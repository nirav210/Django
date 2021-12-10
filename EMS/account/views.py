from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User, Group
from .models import Holiday, Leave, Profile
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, CreateEmployeeForm, CreateHolidayForm, CreateLeaveForm

from django.contrib import messages

from account.decorators import admin_only, allowed_users, unauthenticated_user
# from account.models import extendeduser

@unauthenticated_user
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashbord')
        else:
            messages.info(request, 'Usename OR Password are incorrect')
    
    context = {}
    return render(request, 'account/login.html', context)

def logoutuser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@admin_only
def dashbord(request):
    context = {}
    return render(request, 'account/dashbord.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def employee(request):
    
    detail=Profile.objects.all()

    context = {'detail':detail}
    return render(request, 'account/employee.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def create_employee(request):
    employeegroup = Group.objects.get(name = 'employee')
    if request.method == 'POST':
        createuser = CreateUserForm(request.POST)
        createemployee=CreateEmployeeForm(request.POST)
        
        if createuser.is_valid() and createemployee.is_valid():
            
            user = createuser.save()
            
            profile = createemployee.save(commit=False)
            profile.user = user
            profile.save()
            
            user = createuser.cleaned_data.get('username')
            u = User.objects.get(username=user)
            employeegroup.user_set.add(u)

            messages.success(request, 'Account was created for ' + user)

            return redirect('employee')
        
        else:

            print(createuser.errors)
            print(createemployee.errors)

    else:
        createuser = CreateUserForm()
        createemployee=CreateEmployeeForm()

    context = {'createuser':createuser,
                'createemployee':createemployee}
    return render(request, 'account/create-employee.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def holiday(request):

    detail=Holiday.objects.all()
    context = {'detail':detail}
    return render(request, 'account/holiday.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['employee'])
def emp_holiday(request):

    detail=Holiday.objects.all()
    context = {'detail':detail}
    return render(request, 'account/employee-holiday.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def create_holiday(request):
    if request.method == 'POST':
        createholiday = CreateHolidayForm(request.POST)

        if createholiday.is_valid():
            
            
            createholiday.save()

            messages.success(request, 'Holiday was created')

            return redirect('holiday')
        else:

            print(createholiday.errors)
    else:

        createholiday = CreateHolidayForm()
    context = {'createholiday':createholiday}
    return render(request, 'account/create-holiday.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def leave(request):
    
    detail=Leave.objects.all()
    context = {'detail':detail}

    return render(request, 'account/leave.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['employee'])
def create_leave(request):
    if request.method == 'POST':
        createleave = CreateLeaveForm(request.POST)

        if createleave.is_valid():
            
            leave = createleave.save(commit=False)
            leave.user = request.user
            leave.save()
            createleave.save()

            messages.success(request, 'Holiday was created')

            return redirect('holiday')
        else:

            print(createleave.errors)
    else:
        createleave = CreateLeaveForm()
    context = {'createleave':createleave}
    return render(request, 'account/create-leave.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['employee'])
def emp_leave(request):

    detail=Leave.objects.all()
    context = {'detail':detail}
    return render(request, 'account/employee-leave.html', context)