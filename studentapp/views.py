from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Student


# Create your views here.

def home(request):
    return render(request,"studentapp/home.html")

def application(request):
    if request.method == 'POST':
        Student.objects.create(
            name=request.POST["name"],
            email = request.POST["email"],
            department = request.POST["department"],
            mobile = request.POST["mobile"],
        )
        return HttpResponseRedirect(reverse("studentapp:home"))
    return render(request,"studentapp/apply.html")

def dept(request):
    return render(request,"studentapp/dept.html")


def ece(request):
    data = Student.objects.filter(department__exact="ECE")
    return render(request,"studentapp/ece.html",{"data":data})

def eee(request):
    data = Student.objects.filter(department__exact="EEE")
    return render(request,"studentapp/eee.html",{"data":data})

def cse(request):
    data = Student.objects.filter(department__exact="CSE")
    return render(request,"studentapp/cse.html",{"data":data})

