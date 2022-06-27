from django.http import HttpResponse
from . import models


def home(request):
    return HttpResponse("Hello, world. This is my first project")


def books(request):
    books = models.Book.objects.all()
    return HttpResponse(books)