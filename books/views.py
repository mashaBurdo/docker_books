from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Avg, Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.utils.translation import gettext as _

from . import models
from .forms import *


def home(request):
    return HttpResponse("Hello, world. This is my first project")


def books(request):
    books = models.Book.objects.all()
    context = {"books": books}
    return render(request, "books.html", context)


def book(request, book_id):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            book = get_object_or_404(models.Book, id=book_id)
            text = form.cleaned_data["text"]
            rating = form.cleaned_data["rating"]
            models.Review.objects.create(book=book, text=text, rating=rating)
            return redirect("book", book_id=book.id)
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
            "form": form,
            "reviews_average_rating": reviews_average_rating,
        }
        return render(request, "book.html", context)


def log_in(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(
                username=cleaned_data["username"], password=cleaned_data["password"]
            )
            if user and user.is_active:
                login(request, user)
                return redirect("books")
            else:
                return HttpResponse(_("Something went wrong"))
    else:
        form = LoginForm()
        context = {"form": form, "title": _("Login")}
        return render(request, "form.html", context)


def log_out(request):
    logout(request)
    return redirect("books")


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            if not User.objects.filter(Q(username=form.cleaned_data['username']) | Q(email=form.cleaned_data['email'])):
                user = User.objects.create_user(**form.cleaned_data)
                login(request, user)
                return redirect("books")
            else:
                return HttpResponse(_('user exists'))
    else:
        form = RegistrationForm()
        context = {"form": form, "title": _("Registration")}
        return render(request, "form.html", context)