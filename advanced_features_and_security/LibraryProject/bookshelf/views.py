from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import Permission

# Create your views here.
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