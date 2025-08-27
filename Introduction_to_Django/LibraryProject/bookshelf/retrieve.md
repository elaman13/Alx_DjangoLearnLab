all_books = Book.objects.all()
print(f'Title: {all_books[0].title}\nAuthor: {all_books[0].author}\npublication year: {all_books[0].publication_year}')

'''
Title: 1984
Author: George Orwell
publication year: 198
'''