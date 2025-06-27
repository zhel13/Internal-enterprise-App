from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    context_object_name = 'homepage'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)