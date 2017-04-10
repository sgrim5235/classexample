from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from . models import Person



class HomeView(TemplateView):
    template_name = 'myapp/home.html'

class ProfileView(TemplateView):
    template_name = 'myapp/profile.html'

class PeopleView(ListView):
    template_name = 'myapp/people.html'
    model = Person