from django.db.models import Avg
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

from . import models
from .forms import ReviewForm


def home(request):
    return HttpResponse("Hello, world. This is my first project")


def books(request):
    books = models.Book.objects.all()
    context = {"books": books}
    return render(request, "books.html", context)


def book(request, book_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            book = get_object_or_404(models.Book, id=book_id)
            text = form.cleaned_data['text']
            rating = form.cleaned_data['rating']
            models.Review.objects.create(book=book, text=text, rating=rating)
            return redirect('book', book_id=book.id)
    else:
        book = get_object_or_404(models.Book, id=book_id)
        reviews_average_rating = models.Review.objects.filter(book=book).aggregate(
            Avg("rating")
        )["rating__avg"]
        form = ReviewForm()
        reviews = models.Review.objects.filter(book=book)
        context = {
            "book": book,
            "reviews": reviews,
            'form': form,
            "reviews_average_rating": reviews_average_rating,
        }
        return render(request, "book.html", context)
