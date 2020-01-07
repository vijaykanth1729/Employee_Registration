from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import EmployeeForm
from .models import Employee

def employee_list(request):
    employee_list = Employee.objects.all()
    context = {'employee_list':employee_list}
    return render(request, 'employee_register/list.html', context)

def employee_form(request, id=0):
    if request.method=='POST':
        if id==0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee:list')
    else:
        if id==0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
    return render(request, 'employee_register/form.html', {'form': form})


def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('employee:list')