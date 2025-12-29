class Book:
    def __init__(self, book_id, title, author):
        self.id = book_id
        self.title = title
        self.author = author
        self.available = True

    def mark_as_borrowed(self):
        self.available = False

    def mark_as_returned(self):
        self.available = True
