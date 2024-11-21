from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('admin_dashboard',views.admin_dashboard),
    path('view_clients',views.view_clients),
    path('view_users',views.view_users),
    path('view_projects',views.view_projects),
    path('project_manager_dashboard',views.project_manager_dashboard),
    path('report',views.report),
    path('user_dashboard',views.user_dashboard),
    path('check_login',views.check_login)
]
