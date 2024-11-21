from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('adminclient',views.adminclient),
    path('AdminDashBoard',views.AdminDashBoard)
]
