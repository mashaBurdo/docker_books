from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255, null=True, blank=True)
    price = models.IntegerField()
    pages = models.IntegerField(default=1000)

    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.TextField()
    rating = models.IntegerField(
        default=3, validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Shop(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True, blank=True)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

