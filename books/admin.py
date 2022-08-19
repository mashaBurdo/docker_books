from django.contrib import admin

from .models import *


admin.site.register(Review)
admin.site.register(Shop)


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'price')
    search_fields = ('name', 'author')


admin.site.register(Book, BookAdmin)