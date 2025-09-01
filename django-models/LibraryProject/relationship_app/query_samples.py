from . import models

# All books by a specific Author
author = models.Author(name='Elyas')
all_book_by_author = models.Book.objects.get(author=author)

# All books in a library
library = models.Library(name='Central')
all_book_in_library = library.book.all()

# Retrieve a librarian for a library
librarian = models.Librarian.objects.get(library=library)