'''
	The DB interface for the application. Handles queries and other
	interactions with the database.

	@name	: .\src\database\DBInterface.py
	@author	: Steven Maio
	@date	: 03/08/2019
'''
from src.database.queries import *
from src.database.Book import Book
from src.config.config import DATABASE

import sqlite3
import os
import functools
import operator

'''
'''
class DBInterface:

    def __init__(self, database_name=DATABASE):
        # TODO: Determine if the database already exists
        if os.path.isfile(database_name):
                self.connection = sqlite3.connect(database_name)
        else:
                self.connection = self._init_database(database_name)

    '''
            Helper method which initializes the database for this program (this
            includes the tables, etc.).
    '''
    def _init_database(self, database_name):
        connection = sqlite3.connect(database_name)
        connection.execute(INIT_TABLE_FILES)
        connection.execute(INIT_TABLE_TAGS)
        connection.execute(INIT_TABLE_AUTHORED)
        connection.commit()
        return connection

    '''
        Queries for one result, and returns the result deserialized as a Book.
    '''
    def queryOne(self, file_id):
        parameters = [(file_id)]
        query = self.connection.execute(QUERY_FILE_BY_ID, parameters)
        result = query.fetchone()
        book = Book(row=result)
        return book

    '''
            Inserts a file into the table.
    '''
    def addFile(self, title, authors, genre, location, tags):
        #Change location to absolute location
        location = os.path.abspath(location)
        connection = self.connection
        cursor = connection.cursor()
        # Insert the book into the DB
        args = (title, genre, location)
        cursor.execute(INSERT_FILE, args)
        file_id = cursor.lastrowid
        # Insert each author into the authored table
        for a in authors:
                args = (file_id, a)
                connection.execute(INSERT_AUTHORED, args)
        # Insert each tag into the tags table
        for t in tags:
                args = (file_id, t)
                connection.execute(INSERT_TAG, args)
        return file_id

    '''
            Commits all changes to the database and then closes the connection.
    '''
    def close(self):
        self.connection.commit()
        self.connection.close()
