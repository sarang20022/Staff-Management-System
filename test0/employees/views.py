from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee

def home(request):
    return render(request, 'home.html')

def add_employee(request):
    if request.method == 'POST':
        # Get form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        position = request.POST.get('position')
        department = request.POST.get('department')
        salary = request.POST.get('salary')
        hire_date = request.POST.get('hire_date')
        
        # Create new employee
        Employee.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            position=position,
            department=department,
            salary=salary,
            hire_date=hire_date
        )
        return redirect('employee_list')
    
    return render(request, 'add_employee.html')

def employee_list(request):
    employees = Employee.objects.all()
    
    # Filter by department if specified
    department = request.GET.get('department')
    if department:
        employees = employees.filter(department__icontains=department)
    
    # Filter by position if specified
    position = request.GET.get('position')
    if position:
        employees = employees.filter(position__icontains=position)
    
    # Search by name if specified
    search = request.GET.get('search')
    if search:
        employees = employees.filter(first_name__icontains=search) | employees.filter(last_name__icontains=search)
    
    return render(request, 'employee_list.html', {'employees': employees})

def delete_employee(request, employee_id):
    """View to delete an employee"""
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    
    return render(request, 'confirm_delete.html', {'employee': employee})