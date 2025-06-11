class Book:
    def __init__(self, title, author):
        self.title = title              # Public attribute
        self.author = author            # Public attribute
        self._is_checked_out = False    # Private attribute

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out

    def __str__(self):
        return f"'{self.title}' by {self.author}"


class Library:
    def __init__(self):
        self._books = []  # Private list of Book instances

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)
        else:
            raise ValueError("Only instances of Book can be added.")

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return f"You have checked out {book}."
        return "Book not available for checkout."

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return f"You have returned {book}."
        return "Book not found or wasn't checked out."

    def list_available_books(self):
        available_books = [str(book) for book in self._books if book.is_available()]
        return available_books if available_books else ["No books available."]
    

   
