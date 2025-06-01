import sqlalchemy.orm

engine: sqlalchemy.Engine = sqlalchemy.create_engine(
    url="sqlite:////Users/kuriankevin/Documents/GitHub/money-manager/money_manager.db", future=True)
SessionFactory: sqlalchemy.orm.sessionmaker[sqlalchemy.orm.Session] = sqlalchemy.orm.sessionmaker(
    bind=engine, autoflush=False, autocommit=False, future=True)
Base: sqlalchemy.orm.DeclarativeMeta = sqlalchemy.orm.declarative_base()


def initialize_db() -> None:
    Base.metadata.create_all(bind=engine)
