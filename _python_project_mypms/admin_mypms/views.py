from django.shortcuts import HttpResponse ,render

# Create your views here.
def login(request):
    return render(request,"login.html")

def adminclient(request):
    return render(request,'adminclient.html')

def AdminDashBoard(request):
    return render(request,'AdminDashBoard.html')

def adminProject(request):
    return render(request,'adminProject.html')


def adminUsers(request):
    return render(request,'adminUsers.html')


def projectmanangerdashboard(request):
    return render(request,'projectmanangerdashboard.html')


def reports(request):
    return render(request,'reports.html')

def userdashboard(request):
    return render (request,'userdashboard.html')