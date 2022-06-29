from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from . import models


def home(request):
    return HttpResponse("Hello, world. This is my first project")


def books(request):
    books = models.Book.objects.all()
    context = {'books': books}
    return render(request, 'books.html', context)


def book(request, book_id):
    book = get_object_or_404(models.Book, id=book_id)
    context = {'book': book}
    return render(request, 'book.html', context)
