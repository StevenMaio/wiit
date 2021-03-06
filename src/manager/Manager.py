##  @package src.manager.Manager
#   Contains the Manager class
#
#   /author Steven Maio

from src.database.DBInterface import DBInterface
from src.database.QueryBuilder import QueryBuilder, ConditionType, Table
from src.database.queries import *
from src.config.config import PDF_READER

import subprocess
from prettytable import PrettyTable


##  The manager class used to control the flow of the application
#
class Manager:

    ##  Constructs a Manager instance
    #
    #   Initializes a connection to the database
    def __init__(self):
        ##  The interface through which the application interacts with the
        #   database.
        self._db_interface = DBInterface()

    ##  Starts the program and performs a command based on the value of
    #   action.
    #
    #   @param action The command being performed by wiit
    #   @param kwargs key arguments used by the actions the program supports
    def start(self, action : str, **kwargs):
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

    # Helper method which processes an add command
    def _processAdd(self, title : str, authors : list, genre : str,
            location : str, tags : list, **kwargs):
        queryBuilder = QueryBuilder.createInsertQueryBuilder()
        queryBuilder.setTable(TABLE_FILES)
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

    # Helper method which processes an edit command
    def _processEdit(self):
        # TODO: Implement this
        pass

    # Helper method which processes an delete command
    def _processDelete(self, file_id, title, genre, **kwargs):
        deleteBuilder = QueryBuilder.createDeleteQueryBuilder()
        deleteBuilder.setTable(Table.FILES)
        deleteBuilder.addCondition(column=ATTR_ID,
                                   value=file_id,
                                   condition_type=ConditionType.EQUALITY)
        deleteBuilder.addCondition(column=ATTR_TITLE,
                                   value=title,
                                   condition_type=ConditionType.LIKE)
        deleteBuilder.addCondition(column=ATTR_GENRE,
                                   value=genre,
                                   condition_type=ConditionType.LIKE)
        statement, fields = deleteBuilder.build()
        print(statement)
        rows_deleted = self._db_interface.delete(statement=statement,
                                                 fields=fields)
        print("{} rows deleted".format(rows_deleted))


    # Helper method which processes an search command
    def _processSearch(self, file_id, title, authors, genre, tags, **kwargs):
        queryBuilder = QueryBuilder.createSearchQueryBuilder()
        queryBuilder.setTable(TABLE_FILES)
        queryBuilder.addCondition(column=ATTR_ID,
                                  value=file_id,
                                  condition_type=ConditionType.EQUALITY)
        queryBuilder.addCondition(column=ATTR_TITLE,
                                  value=title,
                                  condition_type=ConditionType.LIKE)
        queryBuilder.addCondition(column=ATTR_GENRE,
                                  value=genre,
                                  condition_type=ConditionType.LIKE)
        query, fields = queryBuilder.build()
        results = self._db_interface.query(query_string=query,
                                           fields=fields)
        table = PrettyTable()
        table.field_names = [
            "ID", "Title", "Authors",
            "Genre", "Tags"
        ]
        if len(results) == 0:
            print("No files were found")
        else:
            for r in results:
                table.add_row(r.toTuple())
            print(table)

    # Helper method which processes opening a file
    def _processOpen(self, file_id, **kwargs):
        result = self._db_interface.queryOne(file_id=file_id)
        location = result.getLocation()
        args = [PDF_READER, location]
        subprocess.Popen(args)
