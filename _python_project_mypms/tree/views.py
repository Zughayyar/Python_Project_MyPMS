from django.shortcuts import HttpResponse ,render, redirect
from . import models

# Create your views here.
def createtree(request):
    context = {
        'elements' : models.get_all_elements(),
        'subelements' : models.get_all_sub_elements(),
        'projects' : models.get_all_projects(),
        'projects_tree' : models.get_project_tree()
    }
    return render(request,"createtree.html", context)

def addelement(request):
    if request.method == "POST":
        models.add_element(request.POST)
        return redirect('/tree/createtree')
    else:
        return HttpResponse("something went wrong!!")

def addsubelement(request):
    if request.method == "POST":
        models.add_sub_element(request.POST)
        return redirect('/tree/createtree')
    else:
        return HttpResponse("something went wrong!!")

def addprojecttree(request):
    if request.method == "POST":
        models.create_check_list(request.POST)
        return redirect('/tree/createtree')
    else:
        return HttpResponse("something went wrong!!")