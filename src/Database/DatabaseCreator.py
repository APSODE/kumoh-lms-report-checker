from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class DatabaseCreator:
    Model = declarative_base()

    def __init__(self, db_name: str):
        self._engine = self._create_engine(db_name = db_name)
        self._session = self._create_session()
        self.Model.query = self._session.query_property()
        self.init_db()

    @staticmethod
    def _create_engine(db_name: str) -> Engine:
        return create_engine(
            f"sqlite:///src\\Database\\{db_name}.db",
            echo = True
        )

    def _create_session(self) -> scoped_session:
        return scoped_session(
            sessionmaker(
                autoflush = False,
                bind = self._engine
            )
        )

    @property
    def Session(self) -> scoped_session:
        return self._session

    @property
    def Engine(self) -> Engine:
        return self._engine

    def init_db(self):
        self.Model.metadata.create_all(bind = self._engine)

