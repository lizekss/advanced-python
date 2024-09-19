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
