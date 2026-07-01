from django.shortcuts import render,get_object_or_404
# from django.http import Http404
from .models import Employee


# Create your views here.
def employee_detail(request, pk):

    # try:
    #     employee = employee.objects.get(pk=pk)
    # except:
    #     raise Http404
    #        ((((((    or    ))))))

    employee = get_object_or_404(Employee,pk=pk)
 
    context = {
        'employee' : employee,
    }
    return render(request,'employee_detail.html',context)
