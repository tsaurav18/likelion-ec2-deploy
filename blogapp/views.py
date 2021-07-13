from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog

# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, id):
    blog = get_object_or_404(Blog, pk=id)
    return render(request, 'detail.html', {'blog':blog})

def new(request): # new.html을 띄워주는 함수
    return render(request, 'new.html')

def create(request): # 입력받은 내용을 데이터베이스에 넣어주는 함수
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.pub_date = timezone.now()
    new_blog.body = request.POST['body']
    new_blog.img = request.FILES['img']
    new_blog.save()
    return redirect('detail', str(new_blog.id))

def edit(request, id):
    edit_blog = Blog.objects.get(id=id)
    return render(request, 'edit.html', {'blog':edit_blog})

def update(request, id):
    update_blog = Blog.objects.get(id=id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.pub_date = timezone.now()
    update_blog.body = request.POST['body']
    update_blog.save()
    return redirect('detail', str(update_blog.id))

def delete(request, id):
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('home')