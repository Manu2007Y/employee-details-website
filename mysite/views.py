from django.shortcuts import render
from django.http import HttpResponse
from employees.models import Employee

def helloWorld(request):
    return HttpResponse('hello world')

def home(request):
    employees = Employee.objects.all()
    context = {
        'employees' : employees
    }

    return render(request,'home.html',context)