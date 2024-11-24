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
        this_checklist = models.get_project_tree_by_filter(project_id, element_id, subelement_id)
        all_tasks_approved = True
        checklist_count = 0
        first_checklist_id = None
        for item in this_checklist:
            checklist_count += 1
            if first_checklist_id == None:
                first_checklist_id = item.id
            if item.checklist == 'Not Approved':
                all_tasks_approved = False
        context = {
            'element1'      : models.get_element_by_id(1),
            'element2'      : models.get_element_by_id(2),
            'subelements'   : models.get_all_sub_elements(),
            'project'       : models.get_project_by_id(project_id),
            'element'       : models.get_element_by_id(element_id),
            'subelement'    : models.get_sub_element_by_id(subelement_id),
            'checklist'     : this_checklist,
            'all_tasks_approved': all_tasks_approved,
            'checklist_count': checklist_count,
            'first_checklist_id': first_checklist_id
        }
        return render(request,'project_checklist.html', context)
    else:
        return redirect('/')
    
def report(request):
    context = {
        'projects_tree' : models.get_project_tree()
    }
    return render(request, "report.html", context)

def change_checklist(request):
    project_id = request.POST['project']
    element_id = request.POST['element']
    subelement_id = request.POST['subelement']
    models.change_checklist_status(request.POST)
    return redirect('/tree/checklist/' + str(project_id) + '/' + str(element_id) + '/' + str(subelement_id)  )