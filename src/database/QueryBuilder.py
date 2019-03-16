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
        self._fields.append(column)

    '''
        Adds a condition to the query.
    '''
    def addCondition(self, key):
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
        # Break if there is no table
        table = self._table
        if table == None:
            return None

        fields = self._fields
        if len(fields) == 0:
            fields_str = '*'
        else:
            fields_str = fields[0]
            for x in fields[1:]:
                fields_str += ', {}'.format(x)

        conditions = self._conditions
        if len(conditions) == 0:
            query_string = QUERY_TEMPLATE_NO_CONDITION.format(table, fields_str)
        else:
            init_condition = QUERY_CONDITION_FINAL.format(conditions[-1])
            conditions_str = None
            for cond in conditions[:-1]:
                if conditions_str is None:
                    conditions_str = QUERY_CONDITION.format(cond, EMPTY_SPACE)
                else:
                    conditions_str = conditions_str.format(QUERY_CONDITION.format(cond, EMPTY_SPACE))

            if conditions_str is None:
                conditions_str = init_condition
            else:
                conditions_str = conditions_str.format(init_condition)
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
