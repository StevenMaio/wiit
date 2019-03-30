##  @package src.database.QueryBuilder
#   \author Steven Maio

from src.database.queries import *
from enum import Enum

##  Conditional enums used to build queries
#
class ConditionType(Enum):
    ##  Indicates equality
    EQUALITY = 1
    ##  Indicates whether the relation is by similarity (this is used for strings)
    LIKE = 2
    ##  Indicates membership in a collection
    IN = 3

##  Enum class representing the tables used by the application
#
class Table(Enum):
    ##  Represents the FILES table in the database
    FILES = 1
    ##  Represents the TAGS table in the database
    TAGS = 2
    ##  Represents the AUTHORS talbe in the database
    AUTHORS = 3

    '''
        Returns a string version of the table name for each enum value
        @value Table enum value
    '''
    ##  Returns the string name of the table based on the enum value
    #
    #   @param value the enum value of the table
    #
    #   @return the name of the table whose enum value is given by **value**
    #   @static
    @staticmethod
    def getString(value : int) -> str:
        if value == Tables.FILES:
            return "FILES"
        elif value == Tables.TAGS:
            return "TAGS"
        elif value == Tables.AUTHORS:
            return "AUTHORS"
        else:
            return None

##  A builder class used to construct querie strings
#
class QueryBuilder:

    INSERT_TEMPLATE = "INSERT INTO {} ({}) VALUES ({})" 
    QUERY_TEMPLATE = "SELECT {} FROM {} WHERE {}"
    DELETE_TEMPLATE = "SELECT {} FROM {} WHERE {}"

    ##  Creates a new instance of an InsertQueryBuilder
    #
    #   @return a recently instantiated InsertQueryBuilder
    @staticmethod
    def createInsertQueryBuilder():
        return InsertQueryBuilder()

    ##  Creates a new instance of an SearchQueryBuilder
    #
    #   @return a recently instantiated SearchQueryBuilder
    @staticmethod
    def createSearchQueryBuilder():
        return SearchQueryBuilder()

##  A builder class used to construct insert queries
#
class InsertQueryBuilder:
        
    def __init__(self):
        self._values = []
        self._table = None

    ##  Sets the value of the table in which a row is being inserted.
    #
    #   @param table an enum value indicating the table in questoin
    def setTable(self, table : Table):
        self._table = Table.getString(table)

    ##  Adds a value to be inserted in the row in the database 
    #
    #   @param column_name The name of the column
    #   @param value The value beinged inserted into the column 
    def addValue(self, column_name : str, value : object):
        self._values.append((column_name, value))

    ##  Builds a query string based on the fields of the QueryBuilder
    #
    #   @return An SQL query to be executed
    def build(self) -> str:
        pass

##  A builder class used to construct search queries
#
class SearchQueryBuilder:

    def __init__(self):
        self._fields = []
        self._conditions = []
        self._table = None

    ##  Sets the table to be queried
    #   
    #   @param table the table being queried
    def setTable(self, table : str):
        self._table = table


    ##  Adds a column to the query result.
    #   
    #   @param column another column retrieved by the search results
    def addColumn(self, column : str):
        if not column is None:
            self._fields.append(column)
        else:
            pass

    ##  Adds a condition to the query.
    #
    #   @param column the being inspected by the condition
    #   @param value the value with which the columns are compared
    #   @param condition_type the binary relation used to filter results
    def addCondition(self, column : str, value : object, condition_type : ConditionType):
        if not column is None:
            self._conditions.append((column, condition_type, value))
        else:
            pass

    ##  Helper method which builds a query string for a search
    #   @return Returns a tuple of the form (query_string, parameters) whose
    #           first element is the query string to be executed by the sql
    def build(self) -> str:
        def get_condition_statement(pair):
            attribute, condition_type, value = pair
            if condition_type == ConditionType.EQUALITY:
                return QUERY_CONDITION_EQUAL.format(attribute)
            else:
                return QUERY_CONDITION_LIKE.format(attribute)

        table = self._table
        fields = self._fields
        conditions = self._conditions
        params = list(map(lambda x: x[2], conditions))

        # Break if there is no table
        if table == None:
            return None

        if len(fields) == 0:
            fields_str = '*'
        else:
            fields_str = fields[0]
            for x in fields[1:]:
                fields_str += ', {}'.format(x)

        if len(conditions) == 0:
            query_string = QUERY_TEMPLATE_NO_CONDITION.format(table, fields_str)
        else:
            conditions_str = get_condition_statement(conditions[0])
            for cond in conditions[1:]:
                conditions_str += AND + get_condition_statement(cond)
            query_string = QUERY_TEMPLATE.format(fields_str, table, conditions_str)

        return query_string, tuple(params)


# DEBUG
if __name__ == '__main__':
    qb = QueryBuilder.createSearchQueryBuilder()
    qb.setTable("FILES")
    qb.addColumn("TITLE")
    qb.addColumn("LOCATION")
    qb.addCondition(key="TITLE",
                    condition_type=ConditionType.LIKE,
                    value="EE")
    qb.addCondition(key="TAG",
                    condition_type=ConditionType.LIKE,
                    value=["Epp"])
    qb.addCondition(key="FILE_ID",
                    condition_type=ConditionType.EQUALITY,
                    value=3)
    print(qb.build())
