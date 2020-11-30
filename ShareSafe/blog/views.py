from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import User,Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import PostModelForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
    form = UserCreationForm
    return render(request, "register.html", {"form": form})

def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        user=authenticate(request,username=username, password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('home')
    return render(request, "login.html")

def logoutUser(request):
    logout(request)
    return redirect('login')


# ********************************************************************

@login_required(login_url='login')
def home(request):
    user = request.user
    print('user is',user.id)
    showPost = Post.objects.all().order_by('-id')
    return render(request, "home.html", {"showPost": showPost})


def addPost(request):
    form=PostModelForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.createdby_id=request.user.pk
        instance.save()
        return redirect("home")
    return render(request, "register.html", {"form": form})


def ParticularPost(request,id):
    print("inside particular q id is", id)
    p = Post.objects.get(id=id)
    img = "https://images.unsplash.com/photo-1560413540-76cbec4affd6"
    return render(request,'ParticularPost.html',{ "post":p,  "img":img})

# Share via email

def myPost(request):
    myPost = Post.objects.filter(createdby_id=request.user.pk)
    print(myPost)
    return render(request,'myPost.html', {"myPost":myPost})
