from library_DAO import SQLiteDAO, SQLAlchemyDAO
import random
import faker

N_AUTHORS = 500
N_BOOKS = 1000

fake = faker.Faker()

# create DAO instance
dao = SQLAlchemyDAO('library.db')


def add_random_author():
    first_name = fake.first_name()
    last_name = fake.last_name()
    birth_date = fake.date_between(start_date='-100y', end_date='-40y')
    birth_place = fake.city()

    dao.insert_author(first_name, last_name, birth_date, birth_place)


def add_random_book(n_authors):
    title = fake.catch_phrase()
    category = fake.word(ext_word_list=None)
    pages = random.randint(100, 1000)
    publication_date = fake.date_between(start_date='-20y', end_date='today')
    author_id = random.randint(1, n_authors)

    dao.insert_book(title, category, pages, publication_date, author_id)


for _ in range(N_AUTHORS):
    add_random_author()

for _ in range(N_BOOKS):
    add_random_book(N_AUTHORS)

print('Book with most pages:', dao.get_book_with_most_pages())
print('Average number of pages:', dao.get_average_pages())
print('Youngest author:', dao.get_youngest_author())

author_without_book = dao.get_author_without_book()
if author_without_book is not None:
    print('Author without a book:', author_without_book)
else:
    print('All authors have at least one book.')

# close the connection
dao.close()
