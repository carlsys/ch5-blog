from django.urls import path
from .views import BlogListView, BlogDetailView, BlogAboutUs, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('blabal/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('about-us/', BlogAboutUs.as_view(), name="blog_about_us"),
    path('create/', BlogCreateView.as_view(), name="blog_create"),
    path('update/<int:pk>', BlogUpdateView.as_view(), name="blog_update"),
    path('delete/<int:pk>', BlogDeleteView.as_view(), name="blog_delete"),
]
