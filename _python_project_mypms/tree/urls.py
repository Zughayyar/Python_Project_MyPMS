from django.urls import path
from . import views

urlpatterns = [
    path('createtree', views.create_tree),
    path('addelement', views.add_element),
    path('addsubelement', views.add_sub_element),
    path('addprojecttree', views.add_project_tree),
    path('checklist/<int:project_id>/<int:element_id>/<int:subelement_id>', views.project_checklist),
]
