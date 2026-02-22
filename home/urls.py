from . import views
from django.urls import path
urlpatterns=[
  path('',views.add_employee,name='login'),
  path('employes/',views.employee_list,name='emplist'),
]