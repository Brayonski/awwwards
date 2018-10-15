from django.shortcuts import render,redirect,get_list_or_404
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm
from .models import Projects,Profile

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    images = Projects.objects.all()
    return render(request,'index.html',{"images":images,})

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
