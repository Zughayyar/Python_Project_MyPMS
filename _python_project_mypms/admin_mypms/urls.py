from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('adminclient',views.adminclient),
    path('AdminDashBoard',views.AdminDashBoard),
    path('adminProject',views.adminProject),
    path('adminUsers',views.adminUsers),
    path('projectmanangerdashboard',views.projectmanangerdashboard),
    path('reports',views.reports),
    path('userdashboard',views.userdashboard)

]
