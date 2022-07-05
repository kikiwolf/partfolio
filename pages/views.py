from re import template
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class PostPageView(TemplateView):
    template_name = 'article_name.html'

class PasswordPageView(TemplateView):
    template_name = 'password_change.html'

class ProfilePageView(TemplateView):
    template_name = 'interface.html'
