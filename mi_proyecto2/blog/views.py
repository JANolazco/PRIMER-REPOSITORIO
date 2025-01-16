from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.shortcuts import render
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    print("Mi home")
    return render(request, 'blog/home.html', context)


def create_post(request):
    print("Funcion create post")
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog-home')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})


