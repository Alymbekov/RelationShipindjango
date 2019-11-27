from django.shortcuts import render

from my_app.models import Author, Biography


def index(request):
    data = Author.objects.all()
    data_of_biography = Biography.objects.all()
    return render(
        request, 'my_app/index.html', {
            'data': data, 'data_of_bio': data_of_biography,
        }
    )

