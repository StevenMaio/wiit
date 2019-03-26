'''
	@author : Steven Maio
	@date : 03/15/2019
'''


'''
    Book class.
'''
class Book:

    def __init__(self, row, authors=[], tags=[], detailed_print=False):
        book_id, title, genre, location = row
        self._book_id = book_id
        self._title = title
        self._genre = genre
        self._location = location
        self._authors = authors
        self._tags = tags
        self._detailed_print = detailed_print

    def __str__(self):
        return 'TITLE: {}; ID: {}; GENRE: {}'.format(self._title, self._book_id, self._genre)

    def getLocation(self) -> str:
        return self._location

    def getTitle(self) -> str:
        return self._title
