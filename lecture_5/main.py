from library_DAO import LibraryDAO
import random
import faker

N_AUTHORS = 500
N_BOOKS = 1000

fake = faker.Faker()

dao = LibraryDAO('library.db')

def add_random_author():
    # Generate a random first name, last name, birthdate, and birthplace
    first_name = fake.first_name()
    last_name = fake.last_name()
    birth_date = fake.date_between(start_date='-100y', end_date='today')
    birth_date = birth_date.strftime('%Y-%m-%d')  # Convert date to string
    birth_place = fake.city()

    dao.insert_author(first_name, last_name, birth_date, birth_place)

def add_random_book(n_authors):
    # Generate a random title, category, number of pages, publication date, and author ID
    title = fake.catch_phrase()
    category = fake.word(ext_word_list=None)
    pages = random.randint(100, 1000)
    publication_date = fake.date_between(start_date='-20y', end_date='today')
    publication_date = publication_date.strftime('%Y-%m-%d')  # Convert date to string
    author_id = random.randint(1, n_authors)

    dao.insert_book(title, category, pages, publication_date, author_id)


for _ in range(N_AUTHORS):
    add_random_author()

for _ in range(N_BOOKS):
    add_random_book(N_AUTHORS)

# Close the connection
dao.close()