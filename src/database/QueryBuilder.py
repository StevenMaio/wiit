'''
    @author: Steven Maio
'''
from src.database.queries import *


class QueryBuilder:

    '''
        Initializes an empty QueryBuilder instance.
    '''
    def __init__(self):
        self._fields = []
        self._conditions = []
        self._table = None

    '''
        Adds a column to the query result.
    '''
    def addColumn(self, column):
        if column is None:
            return
        else:
            self._fields.append(column)

    '''
        Adds a condition to the query.
    '''
    def addCondition(self, key):
        if key is None:
            return
        else:
            self._conditions.append(key)

    '''
        Sets the table which is searched by the query.
    '''
    def setTable(self, table):
        self._table = table

    '''
        Takes in the current fields of the QueryBuilder instance, and produces
        a string of the query.
    '''
    def build(self):
        table = self._table
        fields = self._fields
        conditions = self._conditions

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
            conditions_str = QUERY_CONDITION_FINAL.format(conditions[-1])
            for cond in conditions[:-1]:
                conditions_str += QUERY_CONDITION.format(cond)
            query_string = QUERY_TEMPLATE.format(fields_str, table, conditions_str)

        return query_string


# DEBUG
if __name__ == '__main__':
    qb = QueryBuilder()
    qb.setTable("FILES")
    qb.addColumn("TITLE")
    qb.addColumn("LOCATION")
    qb.addCondition(key="TITLE")
    qb.addCondition(key="TAG")
    qb.addCondition(key="FILE_ID")
    print(qb.build())
