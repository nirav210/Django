from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginpage, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('dashbord/', views.dashbord, name='dashbord'),
    path('dashbord/employee/', views.employee, name='employee'),
    path('dashbord/create-employee/', views.create_employee, name='create-employee'),
    path('dashbord/holiday/', views.holiday, name='holiday'),
    path('dashbord/create-holiday/', views.create_holiday, name='create-holiday'),
    path('dashbord/leave/', views.leave, name='leave'),
    

    path('dashbord/holiday_emp/', views.emp_holiday, name='emp-holiday'),
    path('dashbord/leave_emp/', views.emp_leave, name='emp-leave'),
    path('dashbord/create-leave/', views.create_leave, name='create-leave'),
]