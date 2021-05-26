from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey
from sqlalchemy.orm import relationship

from base import Base

# Definition der N:M-Beziehung
movies_actors_association = Table(
    'movies_actors', Base.metadata,
    Column('movie_id', Integer, ForeignKey('movies.id')),
    Column('actor_id', Integer, ForeignKey('actors.id'))
)

class Movie(Base):
    __tablename__ = 'movies'  # Tabellenname für Persistierung

    # Attribute mit entsprechenden Spaltendefinitionen
    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(Date)

    actors = relationship("Actor", secondary=movies_actors_association)
    
    def __init__(self, title, release_date):
        # die ID wird intern vom ORM verwaltet, kein Attribut, das bei 
        # Objekterzeugung zu übergeben ist
        self.title = title
        self.release_date = release_date