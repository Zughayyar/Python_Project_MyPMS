from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('admin_dashboard',views.admin_dashboard ,name='admin_dashboard'),
    path('view_clients',views.view_clients,name='view_clients'),
    path('view_users',views.view_users,name='view_users'),
    path('view_projects',views.view_projects,name='view_projects'),
    path('project_manager_dashboard',views.project_manager_dashboard,name='project_manager_dashboard'),
    path('report',views.report,name='report'),
    path('user_dashboard',views.user_dashboard,name='user_dashboard'),
    path('contact',views.contact , name='contact'),
    path('about',views.about ,name='about'),
    path('check_login',views.check_login),
    path('logout',views.logout,name='logout'),
    path('add_clinet',views.add_clinet),
    path('add_user',views.add_user),
    path('create_project',views.create_project)
]
