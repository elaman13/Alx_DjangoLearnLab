from . import models

# All books by a specific Author
all_book_by_author = models.Book.objects.get(author='Elyas')

# All books in a library
library = models.Library.objects.get(name='Central').book.all()

# Retrieve a librarian for a library
librarian = models.Librarian.objects.get(library=library)