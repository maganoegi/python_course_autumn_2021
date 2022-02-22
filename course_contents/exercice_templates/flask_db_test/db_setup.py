

import sys 

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

# permet de enchainer les methodes, une chose qu'il en a pas en Python
# les commandes et les requetes de filtrage vont passer par là
Base = declarative_base()



class BookORM( Base ):
    __tablename__ = "book"

    # generé automatiquement
    id = Column(Integer, primary_key=True) 

    # champs de notre table
    title = Column(
        String(250), # type de la valeur et la longueur maximale
        nullable=False # est-ce qu'on est obligé de fournir cette valeur?
        )
    author = Column(String(250), nullable=False)
    genre = Column(String(250))

class Book:
    def __init__(self, title: str, author: str, genre: str):
        self._title = title
        self._author = author
        self._genre = genre

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def genre(self):
        return self._genre

    def orm(self) -> BookORM:
        return BookORM(title=self.title, author=self.author, genre=self.genre)



