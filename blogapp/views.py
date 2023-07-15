#from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from .models import Post

# Create your views here.
class BlogListView(ListView):
    template_name = "bloglistview.html"
    model = Post

class BlogDetailView(DetailView):
    template_name = "blogdetailview.html"
    model = Post

class BlogAboutUs(TemplateView):
    template_name = "aboutus.html"
