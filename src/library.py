from book import Book
from user import User
from loan import Loan
from datetime import date


class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.loans = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_id):
        self.books = [b for b in self.books if b.id != book_id]

    def register_user(self, user):
        self.users.append(user)

    def borrow_book(self, book_id, user_id):
        book = next(b for b in self.books if b.id == book_id)
        user = next(u for u in self.users if u.id == user_id)

        if book.available:
            loan = Loan(book, user, str(date.today()))
            self.loans.append(loan)
            user.loans.append(loan)
            book.mark_as_borrowed()

    def return_book(self, book_id):
        for loan in self.loans:
            if loan.book.id == book_id:
                loan.book.mark_as_returned()
                loan.user.loans.remove(loan)
                self.loans.remove(loan)
                break

    def display_state(self):
        print("Books:")
        for b in self.books:
            print(b.title, "Available:", b.available)

        print("\nLoans:")
        for l in self.loans:
            print(l.book.title, "borrowed by", l.user.name)
