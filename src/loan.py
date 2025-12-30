class Loan:
    def __init__(self, loan_id, book, user):
        self.loan_id = loan_id
        self.book = book
        self.user = user
        self.is_active = True

    def close_loan(self):
        self.is_active = False
        self.book.return_book()

    def __str__(self):
        status = "Active" if self.is_active else "Returned"
        return (
            f"Loan [{self.loan_id}] | "
            f"Book: {self.book.title} | "
            f"User: {self.user.name} | "
            f"Status: {status}"
        )

