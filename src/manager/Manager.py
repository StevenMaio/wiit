'''
'''
from src.database.DBInterface import DBInterface
from src.config.config import PDF_READER

import subprocess


'''
'''
class Manager:

	def __init__(self):
		self._db_interface = DBInterface()

	def start(self, action, **kwargs):
		if action == 'add':
			self._processAdd(**kwargs)
		elif action == 'edit':
			self._processEdit(**kwargs)
		elif action == 'delete':
			self._processDelete(**kwargs)
		elif action == 'search':
			self._processSearch(**kwargs)
		elif action == 'open':
			self._processOpen(**kwargs)
		self._db_interface.close()

	def _processAdd(self, title, authors, genre, location, tags, **kwargs):
		file_id = self._db_interface.addFile(title=title,
						authors=authors,
						genre=genre,
						location=location,
						tags=tags)
		print('File successfully added with id: {}'.format(file_id))

	def _processEdit(self):
		pass

	def _processDelete(self, file_id, **kwargs):
		pass

	def _processSearch(self):
		pass

	'''
		Helper method which processes opening a file
	'''
	def _processOpen(self, file_id, **kwargs):
		result = self._db_interface.queryOne(file_id=file_id)
		location = result[-1]
		args = [PDF_READER, location]
		subprocess.Popen(args)
