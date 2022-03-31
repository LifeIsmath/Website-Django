from django.shortcuts import render


def home(request):
    return render(request, 'migrate/pages/home.html', context={
        'name': 'Blog'
    })
