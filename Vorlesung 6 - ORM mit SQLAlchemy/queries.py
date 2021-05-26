from actor import Actor  # wichtiger Import - Actor-Zugriff im Code
from contact_details import ContactDetails  # wichtiger Import - Mapping von backref
from stuntman import Stuntman # wichtiger Import - Mapping von backref
from movie import Movie

from base import Session

session = Session()

# alle Filme abrufen
movies = session.query(Movie).all()

# Filmdetails anzeigen
for movie in movies:
    print(f'{movie.title} was released on {movie.release_date}')
    for actor in movie.actors:
        # Achtung: contact_details und stuntman existieren nicht in der Datenbank und auch nicht
        # in der Klassendefinition von Actor. 
        # Das Mapping wird automatisch angelegt (über backref)
        print(f"- {actor.name} (stuntman: {actor.stuntman.name}, " \
              f"actor addresses: {' | '.join([cd.address for cd in actor.contact_details])})")
        

                
