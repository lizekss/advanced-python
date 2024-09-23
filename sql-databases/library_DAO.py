import sqlite3
from abc import ABC, abstractmethod

from sqlalchemy import create_engine, func
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import sessionmaker

from entities import Book, Author, Base


class LibraryDAO(ABC):
    @abstractmethod
    def insert_author(self, first_name, last_name, birth_date, birth_place):
        pass

    @abstractmethod
    def insert_book(self, title, category, pages, publication_date, author):
        pass

    @abstractmethod
    def get_book_with_most_pages(self):
        pass

    @abstractmethod
    def get_average_pages(self):
        pass

    @abstractmethod
    def get_youngest_author(self):
        pass

    @abstractmethod
    def get_author_without_book(self):
        pass

    @abstractmethod
    def close(self):
        pass


class SQLiteDAO(LibraryDAO):
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Book(
                ID INTEGER PRIMARY KEY,
                Title TEXT,
                Category TEXT,
                Pages INTEGER,
                PublicationDate DATE,
                AuthorID INTEGER
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Author(
                ID INTEGER PRIMARY KEY,
                FirstName TEXT,
                LastName TEXT,
                BirthDate DATE,
                BirthPlace TEXT
            )
        ''')
        self.conn.commit()

    def insert_book(self, title, category, pages, publication_date, author_id):
        self.cursor.execute('''
            INSERT INTO Book(Title, Category, Pages, PublicationDate, AuthorID)
            VALUES(?,?,?,?,?)
        ''', (title, category, pages, publication_date, author_id))
        self.conn.commit()

    def insert_author(self, first_name, last_name, birth_date, birth_place):
        self.cursor.execute('''
            INSERT INTO Author(FirstName, LastName, BirthDate, BirthPlace)
            VALUES(?,?,?,?)
        ''', (first_name, last_name, birth_date, birth_place))
        self.conn.commit()

    def close(self):
        self.conn.close()

    '''
    it doesn't seem very clean to add these specific functions to the DAO,
    but i still feel like it's better to encapsulate all of the SQL logic here.
    '''

    def get_book_with_most_pages(self):
        self.cursor.execute('SELECT * FROM Book ORDER BY Pages DESC LIMIT 1')
        return self.cursor.fetchone()

    def get_average_pages(self):
        self.cursor.execute('SELECT AVG(Pages) FROM Book')
        return self.cursor.fetchone()[0]

    def get_youngest_author(self):
        self.cursor.execute(
            'SELECT * FROM Author ORDER BY BirthDate DESC LIMIT 1')
        return self.cursor.fetchone()

    def get_author_without_book(self):
        self.cursor.execute('''
            SELECT * FROM Author 
            WHERE ID NOT IN (SELECT DISTINCT AuthorID FROM Book)
            LIMIT 1
        ''')
        return self.cursor.fetchone()


class SQLAlchemyDAO(LibraryDAO):
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
        try:
            return self.session.query(Author).filter(~Author.books.any()).first()
        except NoResultFound:
            return None
