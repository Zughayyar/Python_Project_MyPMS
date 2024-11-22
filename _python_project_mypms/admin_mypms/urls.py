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
    path('contact',views.contact),
    path('about',views.about),
    path('check_login',views.check_login),
    path('logout',views.logout),
    path('add_clinet',views.add_clinet),
    path('add_user',views.add_user),
    path('create_project',views.create_project)
]
