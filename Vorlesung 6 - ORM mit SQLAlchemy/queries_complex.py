from datetime import date

from actor import Actor  # wichtiger Import - Actor-Zugriff im Code
from contact_details import ContactDetails  # wichtiger Import - Mapping von backref
from stuntman import Stuntman # wichtiger Import - Mapping von backref
from movie import Movie

from base import Session

session = Session()

# Filme nach dem 01.01.2015
movies = session.query(Movie) \
    .filter(Movie.release_date > date(2015, 1, 1)) \
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

        

                
