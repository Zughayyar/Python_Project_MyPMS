from django.shortcuts import HttpResponse ,render

# Create your views here.
def createtree(request):
    return render(request,"createtree.html")