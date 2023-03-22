from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
class SignUpJadvalView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('jadval')
    template_name = 'jadval.html'
class SignUp1L1View(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('1L1')
    template_name = '1L1.html'
class SignUpSammuView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('sammu')
    template_name = 'sammu.html'
class SignUpIndexiew(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('index')
    template_name = 'index.html'
