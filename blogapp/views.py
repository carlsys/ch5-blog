#from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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

class BlogCreateView(CreateView):
    template_name = "blogcreateview.html"
    model = Post
    fields = ["title", "author", "body"]

class BlogUpdateView(UpdateView):
    template_name = "blogupdateview.html"
    model = Post
    fields = ["title", "body"]

class BlogDeleteView(DeleteView):
    template_name = "blogdeleteview.html"
    model = Post
    success_url = reverse_lazy("blog_list")

