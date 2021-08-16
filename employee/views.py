from django.shortcuts import render,redirect
from .models import Employee
from .form import Employee_form
# Create your views here.
def employee_list(request):
    employee_list = Employee.objects.all()
    return render(request,'employee_list.html',{'employee_list' : employee_list})

def employee_form(request):
    if(request.method == "GET"):
        #print("hello")
        form = Employee_form()
        return render(request,'employee_form.html',{'form' : form})
    else:
        form = Employee_form(request.POST)
        print(form)
        form.save()
        return redirect('employee_list')

def employee_delete(request,user_id):
    employee = Employee.objects.get(user_id=user_id)
    employee.delete()
    return redirect('employee_list')

def employee_update(request,user_id=0):
    if request.method == "GET":
        if user_id == 0:
            form = Employee_form()
        else:
            employee = Employee.objects.get(user_id=user_id)
            form = Employee_form(instance=employee)
        return render(request, "employee_form.html", {'form': form})
    else:
        if user_id == 0:
            form = Employee_form(request.POST)
        else:
            employee = Employee.objects.get(user_id=user_id)
            form = Employee_form(request.POST,instance= employee)
        #if form.is_valid():
        form.save()
        return redirect('employee_list')


