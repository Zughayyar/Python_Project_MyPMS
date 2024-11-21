from django.shortcuts import HttpResponse ,render

# Create your views here.
def login(request):
    return render(request,"login.html")

def adminclient(request):
    return render(request,'adminclient.html')

def AdminDashBoard(request):
    return render(request,'AdminDashBoard.html')