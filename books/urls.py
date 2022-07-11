from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("books/", views.books, name="books"),
    path("book/<int:book_id>/", views.book, name="book"),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('register/', views.register, name='register'),

]
