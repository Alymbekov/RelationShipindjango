from django.db import models


class Author(models.Model):
    name = models.CharField(
        max_length=100, verbose_name='Name'
    )
    last_name = models.CharField(
        max_length=100, verbose_name='Last name'
    )
    date_birth = models.DateTimeField(
        verbose_name='Date birth'
    )
    famous = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name='The title of the book'
    )
    published = models.DateTimeField(verbose_name='The data of publishing')
    pages = models.PositiveIntegerField(verbose_name='The count of the pages')
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='books', verbose_name='Author'
    )

    def __str__(self):
        return f"{self.author}---{self.title}"

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


class Biography(models.Model):
    description = models.TextField(
        max_length=500
    )
    author = models.OneToOneField(
        Author, on_delete=models.CASCADE,
        primary_key=True,
    )


class Genre(models.Model):
    title = models.CharField(max_length=100)
    book = models.ManyToManyField(
        Book
    )

    def __str__(self):
        return self.title














