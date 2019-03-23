'''@package src.manager.Manager
    Contains the Manager class
'''
from src.database.DBInterface import DBInterface
from src.database.QueryBuilder import QueryBuilder, ConditionType, Command
from src.database.queries import *
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
        # Check for missing arguments
        if title is None\
                or authors is None\
                or genre is None\
                or location is None\
                or tags is None:
            print('Error : Missing arguments')
            return
        file_id = self._db_interface.addFile(title=title,
                                        authors=authors,
                                        genre=genre,
                                        location=location,
                                        tags=tags)
        print('File successfully added with id: {}'.format(file_id))

    def _processEdit(self):
        # TODO: Implement this
        pass

    def _processDelete(self, file_id, **kwargs):
        # TODO: Implement this
        pass

    def _processSearch(self, file_id, title, authors, genre, tags, **kwargs):
        queryBuilder = QueryBuilder()
        queryBuilder.setCommand(Command.SELECT)
        queryBuilder.setTable(TABLE_FILES)
        queryBuilder.addCondition(key=ATTR_ID,
                                  condition_type=ConditionType.EQUALITY
                                  value=file_id)
        queryBuilder.addCondition(key=ATTR_TITLE,
                                  condition_type=ConditionType.LIKE,
                                  value=title)
        queryBuilder.addCondition(key=ATTR_GENRE,
                                  condition_type=ConditionType.LIKE,
                                  value=genre)
        query, fields = queryBuilder.build()
        results = self._db_interface.query(query_string=query,
                                           fields=fields)
        for r in results:
            print(r)

    '''
            Helper method which processes opening a file
    '''
    def _processOpen(self, file_id, **kwargs):
        result = self._db_interface.queryOne(file_id=file_id)
        location = result.getLocation()
        args = [PDF_READER, location]
        subprocess.Popen(args)
