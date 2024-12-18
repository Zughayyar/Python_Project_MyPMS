from django.shortcuts import HttpResponse ,render, redirect
from django.contrib import messages
import admin_mypms.models
from . import models
import tree.models
import math

### login function:
# 1. load login page.
def login(request):
    if 'is_logged_in' not in request.session:
        request.session['is_logged_in'] = False
    return render(request,"login.html")

### admin dashboard function:
# 1. view nav bar 
# 2. view recent project
# 3. List latest 3 modified project
# 4. List of latest 3 project
# Note: admin dashboard can access: view_clients, view_users, view_projects
def admin_dashboard(request):
    if request.session['is_logged_in'] == True:
        context = {
            'latest_projects'   : models.get_projects_ordered_by_last_added(),
            'modified_projects' : models.get_projects_ordered_by_last_modified()
        }
        return render(request,'admin_dashboard.html', context)
    else:
        return redirect('/')

### view clients function:
# 1. view clients table
# 2. include add client form
def view_clients(request):
    if request.session['is_logged_in'] == True:
        context = {
            'clients' : models.get_all_clients()
        }
        return render(request,'view_clients.html', context)
    else:
        return redirect('/')

### view users function:
# 1. view users table
# 2. include add user form
# 3. view department table
# 4. dropdown input for department
def view_users(request):
    if request.session['is_logged_in'] == True:
        context = {
            'users' : models.get_all_users(),
            'departments' : models.get_all_departments()
        }
        return render(request,'view_users.html', context)
    else:
        return redirect('/')

### view projects function:
# 1. view projects table
# 2. include add projects form
# 3. dropdown input for Clinets
# 4. dropdown input for user(Filter project managers)
def view_projects(request):
    if request.session['is_logged_in'] == True:
        context = {
            'clients' : models.get_all_clients(),
            'projects' : models.get_all_projects(),
            'managers' : models.get_all_managers()
        }
        return render(request,'view_projects.html', context)
    else:
        return redirect('/')

### project manager dashboard function:
# 1. view projects trees
# 2. can modify checklist status
def project_manager_dashboard(request):
    if request.session['is_logged_in'] == True:
        projects = admin_mypms.models.get_all_projects_ordered_by_last_added()
        projects_with_checklists = []
        for project in projects:
            checklists_count = tree.models.get_all_checklist_by_project_id(project.id)
            approved_checklists = tree.models.get_only_approved_by_project_id(project.id)
            completion_percentage = math.trunc((approved_checklists / checklists_count) * 100 if approved_checklists != 0 else 0)
            project_data = {
                'project': project,
                'completion_percentage': completion_percentage
            }
            projects_with_checklists.append(project_data)
        context = {
            'projects_with_checklists' : projects_with_checklists,
            'elements'      : tree.models.get_all_elements(),
            'subelements'   : tree.models.get_all_sub_elements(),
            'projects_tree' : tree.models.get_project_tree()
        }
        return render(request,'project_manager_dashboard.html', context)
    else:
        return redirect('/')

### report function:
# 1. view reports
def report(request):
    if request.session['is_logged_in'] == True: 
        return render(request,'report.html')
    else:
        return redirect('/')

### user dashboard function:
# Note: for now we assumed only one user (project manager)
def user_dashboard(request):
    if request.session['is_logged_in'] == True:
        return HttpResponse("This page used by users from different departments")
    else:
        return redirect('/')

## Check login function:
# 1. check the username and password
# 2. redirect to correct dashboard
# 3. save user info in session
# Note for now we have only Admin and Manager dashboard
def check_login(request):
    if request.method == "POST":
        if models.is_user_exist(request.POST):
            if models.is_password_match(request.POST):
                request.session['is_logged_in'] = True
                logged_user = models.get_user_by_username(request.POST)
                if 'logged_username' not in request.session:
                    request.session['logged_username'] = logged_user.username
                if logged_user.department.id == 1:
                    if 'department' not in request.session:
                        request.session['department'] = logged_user.department.id
                    return redirect('/admin_dashboard')
                if logged_user.department.id == 2:
                    if 'department' not in request.session:
                        request.session['department'] = logged_user.department.id
                    return redirect('/project_manager_dashboard')
            else:
                errors = {'password' : "Username and Password not match!"}
                for key, value in errors.items():
                    messages.error(request, value)
                return redirect('/')
        else:
            errors = {'username' : "Username not found!"}
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
    else:
        HttpResponse("Something went wrong!")
  
## logout function:
# 1. flush session
# 2. redirect to login page
def logout(request):
    request.session.flush()
    return redirect("/")

## Add client function:
# 1.create A Clinet
def add_clinet(request):
    if request.method == "POST":
        errors = models.Client.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            models.create_client(request.POST)
        return redirect('/view_clients')
    else:
        return HttpResponse("Something went wrong!")

## Add User function:
# 1.Create user
def add_user(request):
    if request.method == "POST":
        errors = models.User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            models.create_user(request.POST)
        return redirect('/view_users')
    else:
        return HttpResponse("Something went wrong!")
    
## Create project function:
# 1. create a project
def create_project(request):
    if request.method == "POST":
        errors = models.Project.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            models.create_project(request.POST)
        return redirect('/view_projects')
    else:
        return HttpResponse("Something went wrong!")
    
###
def contact(request):
    return render(request, "contact.html")

###
def about(request):
    return render(request, "about.html")

