from library import Library


def main():
    library = Library()

    # ---- Add books ----
    library.add_book("Python Basics", "ahmed")
    library.add_book("Data Science", "mohamed")

    # ---- Register users ----
    library.register_user("Imene")
    library.register_user("amani")

    # ---- Borrow books ----
    library.borrow_book(book_id=1, user_id=1)
    library.borrow_book(book_id=2, user_id=2)

    # ---- Display status ----
    library.display_status()

    # ---- Return a book ----
    library.return_book(book_id=1, user_id=1)

    # ---- Display final status ----
    library.display_status()


if __name__ == "__main__":
    main()
