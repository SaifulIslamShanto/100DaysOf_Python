
# * Write a Library class with no_of_books and books as two instance variables. Write a program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods. Show that your program doesnt persist the books after the program is stopped!

""" 
    * Library class with no_of_books
    * books as two instance variables
"""

""" Here's an example implementation of the Library class in Python, along with a program that demonstrates how to use it:

```python
class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        self.no_of_books += 1

    def print_books(self):
        if self.no_of_books == 0:
            print("The library has no books.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(book)

    def get_no_of_books(self):
        return self.no_of_books


# Create a library
my_library = Library()

# Add books to the library
my_library.add_book("Book 1")
my_library.add_book("Book 2")
my_library.add_book("Book 3")

# Print all books in the library
my_library.print_books()

# Get the number of books in the library
num_books = my_library.get_no_of_books()
print("Number of books in the library:", num_books)
```

When you run this program, it will create a `Library` object, add some books to it, print the books, and display the number of books in the library. However, please note that once the program is stopped, the books added to the library will not persist. If you run the program again, it will start with an empty library. """

# ------------------------
# *https://replit.com/@SaifulIslamShan/64-Day-64-Exercise-6
