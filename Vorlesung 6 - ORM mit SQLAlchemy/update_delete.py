from datetime import date

from actor import Actor  # wichtiger Import - Actor-Zugriff im Code
from contact_details import ContactDetails  # wichtiger Import - Mapping von backref
from stuntman import Stuntman # wichtiger Import - Mapping von backref
from movie import Movie

from base import Session

session = Session()

# Update-Beispiel
movie = session.query(Movie) \
    .filter(Movie.id == 2) \
    .first()

movie.title = 'UPDATED TITLE'


# Delete-Beispiel
session.query(ContactDetails).delete()

session.commit()
session.close()



        

                
