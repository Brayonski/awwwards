from django.shortcuts import render,redirect,get_list_or_404
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm
from .models import Projects,Profile
from datetime import datetime
from django.contrib.auth.models import User
from .forms import ProfileForm

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    images = Projects.objects.all()
    myDate = datetime.now()
    return render(request,'index.html',{"images":images,'date': myDate,})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user

    ordering=['-date_posted']
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect('home')
    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form":form})

@login_required(login_url='/accounts/login/')
def profile(request,  user_id=None):
    if user_id == None:
        user_id=request.user.id
    current_user = User.objects.get(id = user_id)
    user = current_user
    images = Projects.objects.filter(user=current_user)
    profile = Profile.objects.all()

    return render(request, 'profile.html', locals())

@login_required(login_url='/accounts/login/')
def updateprofile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.profile = request.user.profile
            post.save()
            return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'updateprofile.html',{"form":form})

    