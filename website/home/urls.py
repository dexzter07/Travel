from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('inquiry/', views.inquiry, name='inquiry'),
    path('package/', views.package, name='package'),
]
