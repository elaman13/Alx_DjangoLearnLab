from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.contrib.auth.decorators import permission_required

# Create your views here.
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = models.Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

def viewers(request):
    if request.user.has_perm('bookshelf.can_view'):
        return render(request, 'viewers.html')
    else:
        return HttpResponse("Can't access this page!")

def editors(request):
    if request.user.has_perm('bookshelf.can_edit') and not request.user.has_perm('bookshelf.can_delete'):
        return render(request, 'editors.html')
    else:
        return HttpResponse("Can't access this page!")

def admins(request):
    if request.user.has_perm('bookshelf.can_delete'):
        return render(request, 'admins.html')
    else:
        return HttpResponse("Can't access this page!")