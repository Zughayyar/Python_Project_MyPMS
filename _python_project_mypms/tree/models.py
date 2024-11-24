from django.db import models
from admin_mypms.models import Project

## Main tables for checklist tree
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
## get methods:
def get_all_elements():
    return Element.objects.all()

def get_element_by_id(id):
    return Element.objects.get(id=id)

def get_all_sub_elements():
    return SubElement.objects.all()

def get_all_projects():
    return Project.objects.all()

def get_project_tree():
    return ProjectTree.objects.all()

def get_project_by_id(project_id):
    return Project.objects.get(id=project_id)

def get_element_by_id(element_id):
    return Element.objects.get(id=element_id)

def get_sub_element_by_id(subelement_id):
    return SubElement.objects.get(id=subelement_id)

def get_project_tree_by_filter(project_id, element_id, subelement_id):
    return ProjectTree.objects.filter(
        project = get_project_by_id(project_id),
        main_element = get_element_by_id(element_id),
        sub_element = get_sub_element_by_id(subelement_id)
    )

def get_project_tree_by_project(project_id):
    project = Project.objects.get(id=project_id)
    return ProjectTree.objects.filter(project = project)

def get_all_checklist_by_project_id(project_id):
    project = Project.objects.get(id=project_id)
    return ProjectTree.objects.filter(project = project).count()

def get_only_approved_by_project_id(project_id):
    project = Project.objects.get(id=project_id)
    checklist_project = ProjectTree.objects.filter(project=project)
    count_approved = 0
    for item in checklist_project:
        if item.checklist == "Approved":
            count_approved += 1
    return count_approved

#########################################
## add methods:
def add_element(data):
    Element.objects.create(
        main_element = data['main_element']
    )

def add_sub_element(data):
    SubElement.objects.create(
        sub_element = data['sub_element']
    )

def create_check_list(data):
    ProjectTree.objects.create(
        project = Project.objects.get(id=data['project']) ,
        main_element = Element.objects.get(id=data['main_element']),
        sub_element = SubElement.objects.get(id=data['sub_element']),
        description = data['description'],
        checklist = "Not Approved"
    )

#########################################
## update methods:
#Note: This function made by eng. omar rayyan.
def change_checklist_status(data):
    checklist_count = int(data['checklist_count'])
    first_checklist_id = int(data['first_checklist_id'])
    for item in range(first_checklist_id, first_checklist_id + checklist_count):
        checklist_id = int(data[f'checklist_id_{item}'])
        checklist_status = data.get(f'checklist_status_{item}')
        checklist = Checklist.objects.get(id=checklist_id)
        checklist.checklist = 'Not Approved' if not checklist_status else 'Approved'
        print(checklist.checklist, checklist_id)
        checklist.save()

