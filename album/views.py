from django.shortcuts import render,redirect
from django.views.generic import CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .models import AlbumModel
from .forms import AlbumForm
# Create your views here.

@method_decorator(login_required(login_url='login'),name = 'dispatch')
class add_album(CreateView):
    model = AlbumModel
    form_class = AlbumForm
    template_name = "album.html"
    success_url = reverse_lazy('home')

@method_decorator(login_required(login_url='login'),name = 'dispatch')
class edit_album(UpdateView):
    model = AlbumModel
    form_class = AlbumForm
    template_name = "album.html"
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')

@method_decorator(login_required(login_url='login'),name = 'dispatch')
class delete_album(DeleteView):
    model = AlbumModel
    template_name = "del.html"
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')