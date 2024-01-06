from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from moviesORM import Movie, Actor, ContactDetails, Stuntman
import datetime

engine = create_engine("sqlite:///movies.db", echo=False)

with Session(engine) as session:

    # Update-Beispiel
    movie = session.query(Movie) \
        .filter(Movie.id == 2) \
        .first()

    movie.title = 'UPDATED TITLE'

    # Delete-Beispiel
    session.query(ContactDetails).delete()

    session.commit()
    