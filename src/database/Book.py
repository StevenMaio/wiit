##  @package src.database.Book
#
#   Contains the Book class
#   \author Steven Maio


##  A class encaspulting the join of the Files, Tags, and Authored Tables
#
class Book:

    ## Constructs a new instance of a Book
    #
    #   @param row a row in the Files database
    #   @param authors a list of the authors who authored the book identified
    #           by row
    #   @param tags the tags describing the book
    def __init__(self, row, authors=[], tags=[]):
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

    ##  Accessor method for the location field
    #
    #   @return returns the location of the book
    def getLocation(self) -> str:
        return self._location

    ##  Accessor method for the title of the book
    #
    #   @return the title of the book
    def getTitle(self) -> str:
        return self._title
