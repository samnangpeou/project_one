from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from appone.models import *
import bcrypt

# Create your views here.

def index(request):
    return render(request, 'log.html')

def login(request):
    if request.method == 'POST':
        errors = Tenant.objects.log_validator(request.POST)
        if len(errors) > 0:
            for key,values in errors.items():
                messages.error(request,values)
            return redirect('/')
        logged_user = Tenant.objects.filter(username=request.POST['username'])
        if len(logged_user) > 0:
            logged_user = logged_user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['first_name'] = logged_user.first_name
                request.session['user_id'] = logged_user.id
                return redirect('/home')
        messages.error(request, 'Invalid Email/Password')
    return redirect('/')

def home(request):
    if 'first_name' not in request.session:
        return redirect('/')
    context = {
        'user': Tenant.objects.get(id=request.session['user_id']),
        'avail_tasks': Task.objects.filter(done='No'),
        'avail_bills': Bill.objects.filter(done__icontains='No'),
        'avail_reminders': Reminder.objects.filter(done__icontains='No'),
        'tasks': Task.objects.all(),
        'bills': Bill.objects.all(),
        'reminders': Reminder.objects.all(),
    }
    return render(request, 'home.html',context)