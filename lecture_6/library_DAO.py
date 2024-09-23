from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

from entities import Book, Author, Base


class LibraryDAO:
    def __init__(self, db_file):
        engine = create_engine(f'sqlite:///{db_file}')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def insert_book(self, title, category, pages, publication_date, author_id):
        author = self.session.get(Author, author_id)
        book = Book(title=title, category=category, pages=pages,
                    publication_date=publication_date, author=author)
        self.session.add(book)
        self.session.commit()

    def insert_author(self, first_name, last_name, birth_date, birth_place):
        author = Author(first_name=first_name, last_name=last_name,
                        birth_date=birth_date, birth_place=birth_place)
        self.session.add(author)
        self.session.commit()

    def close(self):
        self.session.close()

    def get_book_with_most_pages(self):
        return self.session.query(Book).order_by(Book.pages.desc()).first()

    def get_average_pages(self):
        return self.session.query(func.avg(Book.pages)).scalar()

    def get_youngest_author(self):
        return self.session.query(Author).order_by(Author.birth_date.desc()).first()

    def get_author_without_book(self):
        return self.session.query(Author).filter(~Author.books.any()).first()
