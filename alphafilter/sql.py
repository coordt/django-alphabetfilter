from django.db.models.sql import aggregates
from django.db.models.aggregates import Aggregate


class FirstLetterSQL(aggregates.Aggregate):
    sql_template = 'UPPER(%(function)s(%(field)s, 1, 1))'
    sql_function = 'SUBSTR'


class FirstLetter(Aggregate):
    name = 'FirstLetter'

    def add_to_query(self, query, alias, col, source, is_summary):
        aggregate = FirstLetterSQL(col, source=source, is_summary=is_summary, **self.extra)
        query.aggregates[alias] = aggregate
