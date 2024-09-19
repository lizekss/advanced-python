import sqlite3

class LibraryDAO:
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
                PublicationDate TEXT,
                AuthorID INTEGER
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Author(
                ID INTEGER PRIMARY KEY,
                FirstName TEXT,
                LastName TEXT,
                BirthDate TEXT,
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