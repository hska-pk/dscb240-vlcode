import datetime
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from moviesORM import Movie, Actor, ContactDetails, Stuntman

engine = create_engine("sqlite:///movies.db", echo=True)

with Session(engine) as session:
    
    # 1 - create movies
    bourne_identity = Movie(title="The Bourne Identity", release_date=datetime.date(2002, 10, 11))
    furious_7 = Movie(title="Furious 7", release_date=datetime.date(2015, 4, 2))
    pain_and_gain = Movie(title="Pain & Gain", release_date=datetime.date(2013, 8, 23))

    # 2 - add contact details 
    matt_contact = ContactDetails(phone="415 555 2671", address="Burbank, CA")
    dwayne_contact = ContactDetails(phone="423 555 5623", address="Glendale, CA")
    dwayne_contact_2 = ContactDetails(phone="421 444 2323", address="West Hollywood, CA")
    
    # 3 - create stuntmen
    matt_stuntman = Stuntman(name="John Doe", active=True)
    dwayne_stuntman = Stuntman(name="John Roe", active=True)
    
    # 4 - create actors
    matt_damon = Actor(name="Matt Damon", birthday=datetime.date(1970, 10, 8),
                       contact_details=[matt_contact], stuntman=matt_stuntman)
    dwayne_johnson = Actor(name="Dwayne Johnson", birthday=datetime.date(1972, 5, 2),
                           contact_details=[dwayne_contact, dwayne_contact_2], stuntman=dwayne_stuntman)
    mark_wahlberg = Actor(name="Mark Wahlberg", birthday=datetime.date(1971, 6, 5))
    
    # 5 - add actors to movies
    bourne_identity.actors = [matt_damon]
    furious_7.actors = [dwayne_johnson]
    pain_and_gain.actors = [dwayne_johnson, mark_wahlberg]

    # persist data
    session.add_all([bourne_identity, furious_7, pain_and_gain])
    session.add_all([matt_contact, dwayne_contact, dwayne_contact_2])
    session.add_all([matt_stuntman, dwayne_stuntman])
    session.add_all([matt_damon, dwayne_johnson, mark_wahlberg])    
    
    session.commit()
