from .models import Author, Library, Librarian, Book

# All books by a specific Author
all_book_by_author = Book.objects.get(author='Elyas')

# All books in a library
library_name = 'Central'
library = Library.objects.get(name=library_name)
all_books_in_library = library.book.all()

# Retrieve a librarian for a library
librarian = Librarian.objects.get(library=library)