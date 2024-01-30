from django.shortcuts import render,redirect
from . import views 
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
# Create your views here.


class user_login(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('home')
    def form_valid(self,form):
        return super().form_valid(form)
    def form_invalid(self,form):
        return super().form_invalid(form)
    

def  user_logout(request):
    logout(request)
    return redirect('home')

        
