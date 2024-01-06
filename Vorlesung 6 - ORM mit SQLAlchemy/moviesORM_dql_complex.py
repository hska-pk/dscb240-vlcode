from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from moviesORM import Movie, Actor, ContactDetails, Stuntman
import datetime

engine = create_engine("sqlite:///movies.db", echo=False)

with Session(engine) as session:

    # Filme nach dem 01.01.2015
    movies = session.query(Movie) \
        .filter(Movie.release_date > datetime.date(2015, 1, 1)) \
        .all()

    print('Filme nach dem 1.1.2015:')
    for movie in movies:
        print(f'- {movie.title}')

    # Filme mit Dwayne Johnson
    the_rock_movies = session.query(Movie) \
        .join(Actor, Movie.actors) \
        .filter(Actor.name == 'Dwayne Johnson') \
        .all()

    print('Filme mit Dwayne Johnson:')
    for movie in the_rock_movies:
        print(f'- {movie.title}')


    # Schauspieler, die in Glendale eine Kontaktadresse haben
    glendale_stars = session.query(Actor) \
        .join(ContactDetails) \
        .filter(ContactDetails.address.ilike('%glendale%')) \
        .all()

    print('Schauspieler aus Glendale')
    for actor in glendale_stars:
        print(f'- {actor.name}')

            

                    
