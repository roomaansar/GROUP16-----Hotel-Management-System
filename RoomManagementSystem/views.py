from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.views.generic import TemplateView


class index(TemplateView):
    template_name= 'registration/homepage.html'