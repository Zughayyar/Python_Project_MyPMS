from django.shortcuts import HttpResponse ,render, redirect
from . import models

# Create your views here.
def create_tree(request):
    context = {
        'elements' : models.get_all_elements(),
        'subelements' : models.get_all_sub_elements(),
        'projects' : models.get_all_projects(),
        'projects_tree' : models.get_project_tree()
    }
    return render(request,"createtree.html", context)

def add_element(request):
    if request.method == "POST":
        models.add_element(request.POST)
        return redirect('/tree/createtree')
    else:
        return HttpResponse("something went wrong!!")

def add_sub_element(request):
    if request.method == "POST":
        models.add_sub_element(request.POST)
        return redirect('/tree/createtree')
    else:
        return HttpResponse("something went wrong!!")

def add_project_tree(request):
    if request.method == "POST":
        models.create_check_list(request.POST)
        return redirect('/tree/createtree')
    else:
        return HttpResponse("something went wrong!!")

def project_checklist(request, project_id, element_id, subelement_id):
    if request.session['is_logged_in'] == True:
        context = {
            'project'       : models.get_project_by_id(project_id),
            'element'       : models.get_element_by_id(element_id),
            'subelement'    : models.get_sub_element_by_id(subelement_id),
            'checklist'     : models.get_project_tree_by_filter(project_id, element_id, subelement_id)
        }
        return render(request,'project_checklist.html', context)
    else:
        return redirect('/')