from book import Book
from user import User
from loan import Loan


class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.loans = []

        self.next_book_id = 1
        self.next_user_id = 1
        self.next_loan_id = 1

    # ---------- BOOK MANAGEMENT ----------

    def add_book(self, title, author):
        book = Book(self.next_book_id, title, author)
        self.books.append(book)
        self.next_book_id += 1
        print(f"Book added: {book}")

    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.available:
                    self.books.remove(book)
                    print(f"Book removed: {book}")
                    return
                else:
                    print("Cannot remove a borrowed book.")
                    return
        print("Book not found.")

    # ---------- USER MANAGEMENT ----------

    def register_user(self, name):
        user = User(self.next_user_id, name)
        self.users.append(user)
        self.next_user_id += 1
        print(f"User registered: {user}")

    # ---------- LOAN MANAGEMENT ----------

    def borrow_book(self, book_id, user_id):
        book = self.find_book(book_id)
        user = self.find_user(user_id)

        if not book:
            print("Book not found.")
            return
        if not user:
            print("User not found.")
            return
        if not book.available:
            print("Book is not available.")
            return

        loan = Loan(self.next_loan_id, book, user)
        self.loans.append(loan)
        book.borrow()
        self.next_loan_id += 1

        print(f"Book borrowed successfully:\n{loan}")

    def return_book(self, book_id, user_id):
        for loan in self.loans:
            if (
                loan.book.book_id == book_id
                and loan.user.user_id == user_id
                and loan.is_active
            ):
                loan.close_loan()
                print(f"Book returned successfully:\n{loan}")
                return

        print("Active loan not found.")

    # ---------- DISPLAY ----------

    def display_status(self):
        print("\n--- Books ---")
        for book in self.books:
            print(book)

        print("\n--- Users ---")
        for user in self.users:
            print(user)

        print("\n--- Loans ---")
        for loan in self.loans:
            print(loan)

    # ---------- HELPER METHODS ----------

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def find_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None
