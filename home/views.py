from django.shortcuts import render
from .models import Employee

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees.html', {'employees': employees})



from django.shortcuts import render, redirect
from .form import EmployeeForm

def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST) # Get the typed data
        if form.is_valid():
            form.save() # THIS TRIGGER THE SIGNAL!
            return redirect('emplist')
    else:
        form = EmployeeForm() # Show empty form
        
    return render(request, 'sample.html', {'form': form})

from django.http import HttpResponse
def sample(request):
    return HttpResponse('helo')
