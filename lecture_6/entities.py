from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Book(Base):
    __tablename__ = 'Book'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    category = Column(String)
    pages = Column(Integer)
    publication_date = Column(String)
    author_id = Column(Integer, ForeignKey('Author.id'))

    def __repr__(self):
        return f'Book({self.title}, {self.category}, {self.pages} pages, published {self.publication_date}, author_id {self.author_id})'


class Author(Base):
    __tablename__ = 'Author'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    birth_date = Column(String)
    birth_place = Column(String)

    books = relationship('Book', backref='author')

    def __repr__(self):
        return f'Author({self.first_name} {self.last_name}, born {self.birth_date} in {self.birth_place})'
