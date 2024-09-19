# SQL Database Project
This project is a simple Python application that uses SQLite3 to manage a library database. The database consists of two tables: Author and Book. The Author table stores information about authors, and the Book table stores information about books.
## Getting Started
To run this project, you will need Python 3.6 or later. You will also need the sqlite3 and faker libraries.
`pip install requirements.txt`
## Description
This project uses the DAO (Data Access Object) Design Pattern, in order to separate the data persistence logic in a separate layer.
The main class in this project is LibraryDAO, which encapsulates all interactions with the database.

## Features
The LibraryDAO class provides the following methods:
- `insert_author(name, birth_date, bio)`: Inserts a new author into the Author table.
- `insert_book(title, category, pages, publication_date, author_id)`: Inserts a new book into the Book table.
- `get_all_authors()`: Returns all authors from the Author table.
- `get_all_books()`: Returns all books from the Book table.
- `get_book_with_most_pages()`: Returns the book with the most pages.
- `get_average_pages()`: Returns the average number of pages in all books.
- `get_youngest_author()`: Returns the youngest author.
- `get_author_without_book()`: Returns an author who has not written any books, if one exists.
Remember to always close the database connection when you're done using the close method.

## Usage
Once you've installed the requirements, run
`python main.py`