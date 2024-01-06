from sqlalchemy import create_engine
from moviesORM import Base

engine = create_engine("sqlite:///movies.db", echo=True)
Base.metadata.create_all(engine)