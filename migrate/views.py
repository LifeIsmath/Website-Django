from django.shortcuts import render
from utils.posts.factory import make_post


def home(request):
    return render(request, 'migrate/pages/home.html', context={
        'posts': [make_post() for _ in range(10)],
    })

def post(request, id):
    return render(request, 'migrate/pages/post-view.html', context={
        'post': make_post(),
        'is_detail_page': True,
    })
