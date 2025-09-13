from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_employee, name='add_employee'),
    path('employees/', views.employee_list, name='employee_list'),
    path('delete/<int:employee_id>/', views.delete_employee, name='delete_employee'),
]