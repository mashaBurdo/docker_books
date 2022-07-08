from django.db.models import Avg
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from . import models


def home(request):
    return HttpResponse("Hello, world. This is my first project")


def books(request):
    books = models.Book.objects.all()
    context = {"books": books}
    return render(request, "books.html", context)


def book(request, book_id):
    book = get_object_or_404(models.Book, id=book_id)
    reviews_average_rating = models.Review.objects.filter(book=book).aggregate(
        Avg("rating")
    )["rating__avg"]
    print(reviews_average_rating)
    reviews = models.Review.objects.filter(book=book)
    context = {
        "book": book,
        "reviews": reviews,
        "reviews_average_rating": reviews_average_rating,
    }
    return render(request, "book.html", context)
