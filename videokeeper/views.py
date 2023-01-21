from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView

from videokeeper.forms import UserRegisterForm, UserLoginForm, VideoForm
from videokeeper.models import VideoModel


def add_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        file = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        uploaded_file_url = fs.url(filename)
        form.save()
        return render(request, 'videokeeper/add_video.html', {"uploaded_file_url": uploaded_file_url})
    else:
        form = VideoForm()
    return render(request, 'videokeeper/add_video.html', {"form": form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистраций')
    else:
        form = UserRegisterForm()
    return render(request, 'videokeeper/registration.html', {"form": form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm
    return render(request, 'videokeeper/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


# Create your views here.
class Home(ListView):
    model = VideoModel
    template_name = 'videokeeper/videomodel_list.html'
    context_object_name = "videos"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Videos'
        return context

    def get_queryset(self):
        return VideoModel.objects.all()
