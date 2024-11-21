from django.db import models
from admin_mypms.models import Project

class Checklist(models.Model):
    description = models.TextField()
    checklist = models.TextField(max_length=10, default="Not Approved")

class SubElement(models.Model):
    sub_element = models.TextField()

class Element(models.Model):
    main_element = models.TextField()

class SubElementTree(Checklist):
    sub_element = models.ForeignKey(SubElement, on_delete=models.DO_NOTHING, related_name="sub_element_tree")

class ElementTree(SubElementTree):
    main_element = models.ForeignKey(Element, on_delete=models.DO_NOTHING, related_name="element_tree")

class ProjectTree(ElementTree):
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING, related_name="project_tree")

#########################################
#########################################
def get_all_elements():
    return Element.objects.all()

def add_element(data):
    Element.objects.create(
        main_element = data['sub_element']
    )
#########################################
#########################################
def get_all_sub_elements():
    return SubElement.objects.all()

def add_sub_element(data):
    SubElement.objects.create(
        sub_element = data['sub_element']
    )
#########################################
#########################################
def get_all_projects():
    return Project.objects.all()
#########################################
#########################################
def create_check_list(data):
    ProjectTree.objects.create(
        project = Project.objects.get(id=data['project']) ,
        main_element = Element.objects.get(id=data['main_element']),
        sub_element = SubElement.objects.get(id=data['sub_element']),
        description = data['description'],
        checklist = "Not Approved"
    )

def get_project_tree():
    return ProjectTree.objects.all()
#########################################
#########################################