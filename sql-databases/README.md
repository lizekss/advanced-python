# SQL Database Project
This project is a simple Python application to demonstrate the use of the `SQLite3` and `SQLAlchemy` libraries to manage a library database. The database consists of two tables: Author and Book. The Author table stores information about authors, and the Book table stores information about books.
## Getting Started
To run this project, you will need the SQLLite3, SQLAlchemy and Faker libraries.

`pip install requirements.txt`

## Description
This project uses the DAO (Data Access Object) Design Pattern, in order to separate the data persistence logic in a separate layer.
The main class in this project is LibraryDAO, which encapsulates all interactions with the database.
The project provides two implementations of the abstract LibraryDAO class: `SQLLiteDAO` and `SQLALchemyDAO`

## Features
The LibraryDAO classes provide the following methods:
- `insert_author(name, birth_date, bio)`: Inserts a new author into the Author table.
- `insert_book(title, category, pages, publication_date, author_id)`: Inserts a new book into the Book table.
- `get_book_with_most_pages()`: Returns the book with the most pages.
- `get_average_pages()`: Returns the average number of pages in all books.
- `get_youngest_author()`: Returns the youngest author.
- `get_author_without_book()`: Returns an author who has not written any books, if one exists.
Remember to always close the database connection when you're done using the close method.

## Usage
The `main.py` script initializes the database with 500 random authors and 1000 random books,
then it prints out results of the various database operations.

You can initialize the dao object as either one of `SQLAlchemyDAO` or `SQLLiteDAO`:
```
dao = SQLAlchemyDAO('library.db')
```

Once you've installed the requirements, run
`python main.py`