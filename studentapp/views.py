from django.shortcuts import render
from django.http import HttpResponseRedirect
from models import Student


# Create your views here.

def home(request):
    return render(request,"studentapp/home.html")

def application(request):
    if request.method == 'POST':
        Student.objects.create(
            name=request.POST["name"],
            email = request.POST["email"],
            DEPARTMENT_NAME = request.POST["DEPARTMENT_NAME"],
            mobile = request.POST["mobile"],
        )
      #  return HttpResponseRedirect(reverse("menu:home"))
        return HttpResponseRedirect(reverse("studentapp:apply"))
    return render(request,"studentapp/apply.html")

def dept(request):
    return render(request,"studentapp/dept.html")


def ece(request):
    data = Student.objects.filter()



