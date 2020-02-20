from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.index, name='views'),
    path('blog/blog-post/<int:id>', views.blogpost, name='blog-post'),
]
