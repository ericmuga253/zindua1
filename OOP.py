class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False  # Book is not checked out initially
    def check_out(self):
        self.is_checked_out = True
    def return_book(self):
        self.is_checked_out = False
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Checked Out: {self.is_checked_out}"
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                return
        print("Error: Book not found.")
    def check_out_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.is_checked_out:
                    print("Error: Book already checked out.")
                else:
                    book.check_out()
                    print("Book checked out successfully.")
                return
        print("Error: Book not found.")
    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.is_checked_out:
                    book.return_book()
                    print("Book returned successfully.")
                else:
                    print("Error: Book is not checked out.")
                return
        print("Error: Book not found.")
    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(book)
# Example usage:
# Create some books
book1 = Book("The Catcher in the Rye", "J.D. Salinger", "9780316769488")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")
book3=Book('100m leads','Alex Hermozi','2580061120084')
book4=Book('Batman','Bob Kane','9761862140086')
book5=Book('Unpluged Aplha','Richard Cooper','9764861120084')
# Create a library
library = Library()
# Add books to the library
library.add_book(book1)
library.add_book(book2)
# List all books in the library
library.list_books()
# # Check out a book
# library.check_out_book("9780316769488")
# # List all books in the library after checking out
# library.list_books()
# # Return a book
# library.return_book("9780316769488")
# # List all books in the library after returning
# library.list_books()

# print(book1._str_())
print(library.check_out_book('9780316769488'))
