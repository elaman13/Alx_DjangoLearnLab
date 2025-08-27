from bookshelf.models import Book

delete_book = Book.objects.all()
delete_book[0].delete()
all_books = Book.objects.all()
print(all_books

'''
<QuerySet []>
'''

