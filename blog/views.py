from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post

# Create your views here.
def index(request):
    posts_list = Post.objects.all().order_by('-published')
    paginator = Paginator(posts_list, 5)

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    context  = {'posts': posts}
    return render(request, 'blog/index.html', context)

# View details
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)