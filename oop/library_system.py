class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size
    
    def __str__(self):
        return f"{self.title} by {self.author}, File Size: {self.file_size}kB"
    
class PrintBook(Book):
    def __init__(self, title: str, author: str, pages: int):
        super().__init__(title, author)
        self.pages = pages 
    
    def __str__(self):
        return f"{self.title} by {self.author}, Pages Count: {self.pages}"

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book: Book):
        self.books.append(book)
    
    def list_books(self):
        for book in self.books:
            print(book)
    
    def find_book(self, title: str):
        for book in self.books:
            if book.title == title:
                return book
        return None
    
    def remove_book(self, title: str):
        book = self.find_book(title)
        if book:
            self.books.remove(book)
            print(f"Removed: {book}")
        else:
            print(f"Book '{title}' not found in the library.")