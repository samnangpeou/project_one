from django.shortcuts import render, redirect
from django.contrib import messages
from appone.models import *
from login import *
from django.db.models import Sum

# Create your views here.

def logout(request):
    request.session.flush()
    return redirect('/')

def tasks(request):
    context = {
        'completed': Task.objects.filter(done__icontains='Yes'),
        'avail': Task.objects.filter(done__icontains='No'),
    }
    return render(request, 'tasks.html', context)

def bills(request):
    context = {
        'paid': Bill.objects.filter(done__icontains='Yes'),
        'unpaid': Bill.objects.filter(done__icontains='No'),
        'total_bills': Bill.objects.filter(done__icontains='No').aggregate(Sum('amount'))
    }
    print(Bill.objects.filter(done__icontains='No').aggregate(Sum('amount')))
    return render(request, 'bills.html', context)

def reminders(request):
    context = {
        'completed': Reminder.objects.filter(done__icontains='Yes'),
        'avail': Reminder.objects.filter(done__icontains='No')
    }
    return render(request, 'reminders.html', context)

def addtask(request):
    if request.method == 'POST':
        errors = Task.objects.task_validator(request.POST)
        if len(errors) > 0:
            for key, values in errors.items():
                messages.error(request, values)
            return render(request, 'tasks.html')
        Task.objects.create(
            title=request.POST['title'],
            desc=request.POST['desc'],
            addedby=Tenant.objects.get(id=request.session['user_id']),
            done='No'
        )
        return redirect('/home/tasks')
    return render(request, 'tasks.html')

def addbill(request):
    if request.method == 'POST':
        errors = Bill.objects.bill_validator(request.POST)
        if len(errors) > 0:
            for key, values in errors.items():
                messages.error(request, values)
            return render(request, 'bills.html')
        Bill.objects.create(
            collector=request.POST['collector'],
            amount=request.POST['amount'],
            duedate=request.POST['duedate'],
            addedby=Tenant.objects.get(id=request.session['user_id']),
            done='No'
        )
        return redirect('/home/bills')
    return render(request, 'bills.html')

def addreminder(request):
    if request.method == 'POST':
        errors = Reminder.objects.reminder_validator(request.POST)
        if len(errors) > 0:
            for key, values in errors.items():
                messages.error(request, values)
            return render(request, 'reminders.html')
        Reminder.objects.create(
            title = request.POST['title'],
            desc = request.POST['desc'],
            date = request.POST['date'],
            addedby=Tenant.objects.get(id=request.session['user_id']),
            done = 'No',
        )
        return redirect('/home/reminders')
    return render(request, 'reminders.html')

def edittask(request,id):
    if request.method == 'POST':
        errors = Task.objects.task_validator(request.POST)
        if len(errors) > 0:
            for key, values in errors.items():
                messages.error(request, values)
            return render(request, 'tasks.html')
        update = Task.objects.get(id=id)
        update.title = request.POST['title']
        update.desc = request.POST['desc']
        update.save()
        return redirect('/home/tasks')
    return render(request, 'tasks.html')

def dotask(request,id):
    to_do = Task.objects.get(id=id)
    to_do.done = 'Yes'
    to_do.save()
    return redirect('/home/tasks')

def undotask(request,id):
    undo = Task.objects.get(id=id)
    undo.done = 'No'
    undo.save()
    return redirect('/home/tasks')

def paybill(request,id):
    to_pay = Bill.objects.get(id=id)
    to_pay.done = 'Yes'
    to_pay.save()
    return redirect('/home/bills')

def editbill(request,id):
    if request.method=='POST':
        errors = Bill.objects.bill_validator(request.POST)
        if len(errors) > 0:
            for key, values in errors.items():
                messages.error(request, values)
            return render(request, 'bills.html')
        update = Bill.objects.get(id=id)
        update.collector = request.POST['collector']
        update.amount = request.POST['amount']
        update.duedate = request.POST['duedate']
        update.save()
        return redirect('/home/bills')
    return render(request, 'bills.html')

def removereminder(request,id):
    Reminder.objects.get(id=id).delete()
    return redirect('/home/reminders')

def editreminder(request,id):
    if request.method == 'POST':
        errors = Reminder.objects.reminder_validator(request.POST)
        if len(errors) > 0:
            for key, values in errors.items():
                messages.error(request, values)
            return render(request, 'reminder.html')
        update = Bill.objects.get(id=id)
        update.title = request.POST['title']
        update.desc = request.POST['desc']
        update.date = request.POST['date']
        update.save()
        return redirect('/home/reminders')
    return render(request, 'reminder.html')

def deletetask(request,id):
    Task.objects.get(id=id).delete()
    return redirect('/home/tasks')

def deletebill(request,id):
    Bill.objects.get(id=id).delete()
    return redirect('/home/bills')