from django.shortcuts import HttpResponse ,render, redirect
from . import models
import tree.models

### login function:
# 1. load login page.
def login(request):
    
    return render(request,"login.html")

### admin dashboard function:
# 1. view nav bar 
# 2. view recent project
# 3. List latest 3 modified project
# 4. List of latest 3 project
# Note: admin dashboard can access: view_clients, view_users, view_projects
def admin_dashboard(request):

    return render(request,'admin_dashboard.html')

### view clients function:
# 1. view clients table
# 2. include add client form
def view_clients(request):
    context = {
        'clients' : models.get_all_clients()
    }
    return render(request,'view_clients.html', context)

### view users function:
# 1. view users table
# 2. include add user form
# 3. view department table
# 4. dropdown input for department
def view_users(request):
    context = {
        'users' : models.get_all_users()
    }
    return render(request,'view_users.html', context)

### view projects function:
# 1. view projects table
# 2. include add projects form
# 3.  dropdown input for Clinets
# 4. dropdown input for user(Filter project managers)
def view_projects(request):
    context = {
        'projects' : models.get_all_projects()
    }
    return render(request,'view_projects.html', context)

### project manager dashboard function:
# 1. view projects trees
# 2. can modify checklist status
def project_manager_dashboard(request):
    context = {
        'projects' : models.get_all_projects(),
        'elements' : tree.models.get_all_elements(),
        'subelements' : tree.models.get_all_sub_elements(),
        'projects_tree' :tree.models.get_project_tree()
    }
    return render(request,'project_manager_dashboard.html', context)

### report function:
# 1. view reports
def report(request):
    return render(request,'report.html')

### user dashboard function:
# Note: for now we assumed only one user (project manager)
def user_dashboard(request):
    return HttpResponse("This page used by users from different departments")

## Check login function:
# 1. check the username and password
# 2. redirect to correct dashboard
# 3. save user info in session
# Note for now we have only Admin and Manager dashboard
def check_login(request):
    pass
  
## logout function:
# 1. flush session
# 2. redirect to login page
def logout(request):
    request.session.flush()
    return redirect("/")

## Add client function:
# 1.create A Clinet
def add_clinet(request):
    pass

## Add User function:
# 1.Create user
def add_user(request):
    pass

## Create project function:
# 1. create a project
def create_project(request):
    pass

###
def contact(request):
    return render(request, "contact.html")

###
def about(request):
    return render(request, "about.html")

