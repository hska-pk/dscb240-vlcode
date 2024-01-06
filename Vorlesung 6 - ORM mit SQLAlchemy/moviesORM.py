from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
import datetime

class Base(DeclarativeBase):
    pass


# Definition der N:M-Beziehung zwischen Movie und Actor
movies_actors_association = Table(
    'movies_actors', Base.metadata,
    Column('movie_id', ForeignKey('movies.id'), primary_key=True),
    Column('actor_id', ForeignKey('actors.id'), primary_key=True)
)

class Movie(Base):
    __tablename__ = "movies"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(30))
    release_date: Mapped[Optional[datetime.date]]
    actors: Mapped[List["Actor"]] = relationship(secondary=movies_actors_association, 
                                               back_populates='movies')

    def __str__(self):
        return f"Movie: {self.title} with actors: {'| '.join([str(a) for a in self.actors])}"

class Actor(Base):
    __tablename__ = "actors"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    birthday: Mapped[datetime.date]

    contact_details: Mapped[Optional[List["ContactDetails"]]] = relationship(back_populates="actor")
    stuntman: Mapped[Optional["Stuntman"]] = relationship(back_populates="actor")

    movies: Mapped[List["Movie"]] = relationship(secondary=movies_actors_association, 
                                               back_populates='actors')

    def __str__(self):
        return f"Actor: {self.name} with contact details {'| '.join([str(cd) for cd in self.contact_details])}"\
                f" and stuntman {self.stuntman}"
        
class ContactDetails(Base):
    __tablename__ = "contactdetails"
    id: Mapped[int] = mapped_column(primary_key=True)
    phone: Mapped[str]
    address: Mapped[str]

    actor_id: Mapped[Optional[int]] = mapped_column(ForeignKey("actors.id"))
    actor: Mapped["Actor"] = relationship(back_populates="contact_details")

    def __str__(self):
        return f"ContactDetails: {self.address}"

class Stuntman(Base):
    __tablename__ = "stuntmen"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    active: Mapped[bool]

    actor_id: Mapped[Optional[int]] = mapped_column(ForeignKey("actors.id"))
    actor: Mapped["Actor"] = relationship(back_populates="stuntman")

    def __str__(self):
        return f"Stuntman: {self.name} active: {self.active}"