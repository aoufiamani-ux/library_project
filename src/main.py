from library import Library
from book import Book
from user import User

lib = Library()

book1 = Book(1, "Python Basics", "Guido")
user1 = User(1, "Imene")

lib.add_book(book1)
lib.register_user(user1)

lib.borrow_book(1, 1)
lib.display_state()

lib.return_book(1)
lib.display_state()
