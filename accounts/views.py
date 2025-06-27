from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import CustomUserCreationForm


# Create your views here.
class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = '#add the html'
    success_url = reverse_lazy('index')