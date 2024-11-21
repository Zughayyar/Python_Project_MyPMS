from django.urls import path
from . import views

urlpatterns = [
    path('createtree', views.createtree),
    path('addelement', views.addelement),
    path('addsubelement', views.addsubelement),
    path('addprojecttree', views.addprojecttree),
]
