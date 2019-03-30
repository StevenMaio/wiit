##  The DB interface for the application. Handles queries and other
#   interactions with the database.
#
#   \author Steven Maio

from src.database.queries import *
from src.database.Book import Book
from src.config.config import DATABASE

import sqlite3
import os

## A class which interacts with a database
#
class DBInterface:

    ##  Constructs a new instance of DBInterface. Initializes a connection with
    #   the database specified in the configuration
    #
    #   @param database_name the path to the database
    def __init__(self, database_name=DATABASE):
        # Determine if the database already exists, and create one if it
        # doesn't
        if os.path.isfile(database_name):
            self.connection = sqlite3.connect(database_name)
        else:
            self.connection = self._init_database(database_name)

    #   Helper method which initializes the database for this program (this
    #   includes the tables, etc.).
    #
    #   @param database_name The name of the database
    def _init_database(self, database_name : str) -> sqlite3.Connection:
        connection = sqlite3.connect(database_name)
        connection.execute(INIT_TABLE_FILES)
        connection.execute(INIT_TABLE_TAGS)
        connection.execute(INIT_TABLE_AUTHORED)
        connection.commit()
        return connection

    ##  Queries for a specific entry in the files table
    #
    #   @param file_id the id of the entry in the database
    def queryOne(self, file_id : int) -> Book:
        parameters = [(file_id)]
        query = self.connection.execute(QUERY_FILE_BY_ID, parameters)
        result = query.fetchone()
        book = Book(row=result)
        return book

    ##  Queries for results based on the arguments given.
    #
    #   @param query_string the query to be executed
    #   @param fields the valued used in prepared statements
    def query(self, query_string, fields=()) -> list:
        query = self.connection.execute(query_string, fields)
        results = list(map(lambda x: Book(row=x), query.fetchall()))
        return results

    ##  Inserts a file into the table.
    #   
    #   @param title the title of the entry being added
    #   @param authors a list of the authors of the entry
    #   @param genre the genre of the entry being added
    #   @param location the path to the file
    #   @param tags a list of the tags describing the entry
    def addFile(self, title : str, authors : list, genre : str,
            location : str, tags : list) -> int:
        #Change location to absolute location
        location = os.path.abspath(location)
        connection = self.connection
        cursor = connection.cursor()
        #Insert the book into the DB
        args = (title, genre, location)
        cursor.execute(INSERT_FILE, args)
        file_id = cursor.lastrowid
        #Insert each author into the authored table
        for a in authors:
            args = (file_id, a)
            connection.execute(INSERT_AUTHORED, args)
        #Insert each tag into the tags table
        for t in tags:
            args = (file_id, t)
            connection.execute(INSERT_TAG, args)
        return file_id

    ##  Commits all changes to the database and then closes the connection.
    def close(self):
        self.connection.commit()
        self.connection.close()
