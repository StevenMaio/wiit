'''
    @author: Steven Maio
'''
from src.database.queries import *
from enum import Enum


class ConditionType(Enum):
    EQUALITY = 1
    LIKE = 2
    IN = 3


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
    def addCondition(self, key, condition_type):
        if key is None:
            return
        else:
            self._conditions.append((key, condition_type))

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
        def get_condition_statement(pair):
            attribute, condition_type = pair
            if condition_type == ConditionType.EQUALITY:
                return QUERY_CONDITION_EQUAL.format(attribute)
            else:
                return QUERY_CONDITION_LIKE.format(attribute)

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
            conditions_str = get_condition_statement(conditions[0])
            for cond in conditions[1:]:
                conditions_str += AND + get_condition_statement(cond)
            query_string = QUERY_TEMPLATE.format(fields_str, table, conditions_str)

        return query_string


# DEBUG
if __name__ == '__main__':
    qb = QueryBuilder()
    qb.setTable("FILES")
    qb.addColumn("TITLE")
    qb.addColumn("LOCATION")
    qb.addCondition(key="TITLE", condition_type=ConditionType.LIKE)
    qb.addCondition(key="TAG", condition_type=ConditionType.LIKE)
    qb.addCondition(key="FILE_ID", condition_type=ConditionType.EQUALITY)
    print(qb.build())
