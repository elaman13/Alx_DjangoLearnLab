from . import models

book = models.Book.objects.all()

library = models.Library.objects.get(name='Elyas')

librarian = models.Librarian.objects.get(name='Elyas')