from contextvars import Context
from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import CreateForm
from django.core.paginator import Paginator



def home(request):
    posts=Post.objects.all()
    moses=Paginator(posts, 2)
    page_number=request.GET.get('page')
    page=moses.get_page(page_number)
    Context = {
        'Posts':posts,
        'page':page
    }

    return render(request,"blog/Home.html",Context)
    
def you(request):
    return render(request,"blog/about.html",{'title':'Nikolai Doringoyan'})


@login_required
def CreateNewPost(request):
    form=CreateForm()
    if request.method == 'POST':
        form=CreateForm(request.POST,request.FILES)
        profile=request.user
        if form.is_valid():
            a=form.save(commit=False)
            a.author=profile
            a.save()
            return redirect('blog-home')
    context={
        'form':form
    }
    
    return render(request,'blog/post.html',context)


def new(request):
    return render(request,"blog/what.html")

def readpost (request,pk):
    post=Post.objects.get(id=pk)
    context={'post':post}
    return render(request,'blog/viewpost.html',context)


def updatepost (request,pk):
    post=Post.objects.get(id=pk)
    form=CreateForm(instance=post)
    if request.method == 'POST':
        form=CreateForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog-home')
    context={
        'form':form
    }
    return render(request,'blog/post.html',context)


def deletepost (request,pk):
    post=Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog-home')
    context={'post':post}
    return render(request,'blog/delete.html',context)