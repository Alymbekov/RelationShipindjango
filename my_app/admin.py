from django.contrib import admin

from my_app.models import Author, Book, Biography, Genre

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Biography)
admin.site.register(Genre)



