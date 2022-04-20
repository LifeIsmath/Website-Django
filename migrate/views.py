from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render
from utils.posts.factory import make_post

from .models import Post


def home(request):  
    posts = Post.objects.filter(is_published=True,
                                ).order_by('-id')
    
#------------------------------------
    # posts = get_list_or_404(
    #         Post.objects.filter(
    #         is_published=True,    
    #     ).order_by('-id')
    # )
#------------------------------------
        
    return render(request, 'migrate/pages/home.html', context={
        'posts': posts,
    })
    
def category(request, category_id):
    
#------ More method --------------------------------------  
    # posts = Post.objects.filter(
    #     category__id=category_id, is_published=True).order_by('-id') 
    
    # if not posts: 
    #     raise Http404('Not found ')
#-------------------------------------------------------     
    posts = get_list_or_404(Post.objects.filter(
            category_id=category_id,
            is_published=True,    
        ).order_by('-id')
    )
    
    return render(request, 'migrate/pages/category.html', context={
        'posts': posts,
        'title': f"{posts[0].category.name} - Category | "
    })    

def post(request, id):
    # post = Post.objects.filter(
    #         pk=id,
    #         is_published=True,    
    # ).order_by('-id').first()
    
    post = get_object_or_404(Post, pk=id, is_published=True,)
    
    return render(request, 'migrate/pages/post-view.html', context={
        'post': post,
        'is_detail_page': True,
    })
    
def search(request):
    search_term = request.GET.get('q', '').strip()
    
    if not search_term:
        raise Http404()
    
    return render(request, 'migrate/pages/search.html', {
        'page_title': f'Search for "{search_term}" | ',
    })
