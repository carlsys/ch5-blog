from django.urls import path
from .views import BlogListView, BlogDetailView, BlogAboutUs

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('blabal/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('about-us/', BlogAboutUs.as_view(), name="blog_about_us")
]

