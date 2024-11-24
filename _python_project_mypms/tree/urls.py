from django.urls import path
from . import views

urlpatterns = [
    path('create_tree', views.create_tree),
    path('add_element', views.add_element),
    path('add_sub_element', views.add_sub_element),
    path('add_project_tree', views.add_project_tree),
    path('checklist/<int:project_id>/<int:element_id>/<int:subelement_id>', views.project_checklist),
    path('report/<int:project_id>', views.report),
    path('change_checklist', views.change_checklist)
]
