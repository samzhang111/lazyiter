import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import MetaData


class LazyIterator(object):
    def __init__(self, db_uri, table, columns=None, yield_per=100):
        engine = sqlalchemy.create_engine(db_uri)
        Session = sessionmaker(bind=engine)
        self.session = Session()
        metadata = MetaData()
        metadata.reflect(bind=engine)

        self.table = metadata.tables[table]
        self.columns = columns

    def __iter__(self):
        if not self.columns:
            query = [self.table]
        else:
            query = [self.table.c[column] for column in self.columns]

        cursor = self.session.query(*query).yield_per(10).enable_eagerloads(False)
        self._cursor_iter = iter(cursor)

        return self

    def __next__(self):
        return next(self._cursor_iter)

