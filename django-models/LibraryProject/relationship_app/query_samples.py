from . import models

book = models.Book.objects.all()

book_in_library = models.Library.objects.all()

librarian = models.Librarian.objects.all()