from collections import OrderedDict
from itertools import groupby

from django.db import connections

TABLE_IDS = tuple(('B01002', 'B03002', 'B19301', 'B19013', 'B19001', 'B17001', 'B08006',
    'B08013', 'B08006', 'B12001', 'B09002', 'B13016', 'B11001', 'B11002',
    'B25002', 'B25024', 'B25003', 'B25026', 'B07003', 'B25077', 'B25075',
    'B15002', 'B05002', 'B05006', 'B16001', 'B16007', 'B21002', 'B21001'))

class CensusUS(object):
    def __init__(self, zip=None, *args, **kwargs):
        self.cursor = connections['us_census'].cursor()
        if zip:
            self.geoid = '86000US{zip}'.format(zip=zip)
        else:
            self.geoid = None

    def map_table_defs(self):
        """
        Mapping table definitions
        """
        self.cursor.execute(
            """
            SET search_path TO acs2014_1yr, public;
            SELECT tab.table_id,
                tab.table_title,
                tab.universe,
                tab.denominator_column_id,
                col.column_id,
                col.column_title,
                col.indent
            FROM census_column_metadata col
            LEFT JOIN census_table_metadata tab USING (table_id)
            WHERE table_id IN {TABLE_IDS}
            ORDER BY column_id;""".format(TABLE_IDS=TABLE_IDS)
            )
        result = self.cursor.fetchall()
        valid_table_ids = []
        table_metadata = OrderedDict()

        for table, columns in groupby(result, lambda x: (x[0], x[1], x[2], x[3])):
            valid_table_ids.append(table[0])
            table_metadata[table[0]] = OrderedDict([
                ("title", table[1]),
                ("universe", table[2]),
                ("denominator_column_id", table[3]),
                ("columns", OrderedDict([(
                    column[4],
                    OrderedDict([
                        ("name", column[5]),
                        ("indent", column[6])
                    ])
                ) for column in columns]))
            ])
        self.valid_table_ids = valid_table_ids
        self.meta = table_metadata

    def build_sql_statement(self):
        self.map_table_defs()
        from_stmt = '%s_moe' % (self.valid_table_ids[0])
        if self.valid_table_ids > 1 and self.geoid:
            from_stmt += ' '
            from_stmt += ' '.join(["""JOIN {table_id}_moe USING (geoid)""".format(
                table_id=table_id) for table_id in self.valid_table_ids[1:]])
            print from_stmt

        self.sql_statement = """SELECT * FROM {from_stmt} WHERE geoid='{geoid}'""".format(
            from_stmt=from_stmt, geoid=self.geoid)

