from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from moviesORM import Movie, Actor, ContactDetails, Stuntman
from sqlalchemy import select
import datetime

engine = create_engine("sqlite:///movies.db", echo=False)

with Session(engine) as session:
    stmt = select(Movie).where(Movie.title.contains('n'))
    print("Movies that contain the letter 'n'")
    for movie in session.scalars(stmt):
        print(movie)

    
    stmt = select(Movie).where(Movie.release_date >= datetime.date(2010,1,1))
    print("Movies released after 2010-01-01:")
    for movie in session.scalars(stmt):
        print(movie)

    print("All actors:")
    for actor in session.scalars(select(Actor)):
        print(actor)

    # alle Filme abrufen
    movies = session.query(Movie).all()
    # Filmdetails anzeigen
    for movie in movies:
        print(f'{movie.title} was released on {movie.release_date}')
        for actor in movie.actors:
            # Achtung: contact_details und stuntman existieren nicht in der Datenbank und auch nicht
            # in der Klassendefinition von Actor. 
            # Das Mapping wird automatisch angelegt (über backref)
            print(f"- {actor.name}, " \
                f"actor addresses: {' | '.join([cd.address for cd in actor.contact_details])}")
