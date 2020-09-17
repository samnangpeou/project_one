from django.db import models
from login.models import Tenant

# Create your models here.

class TaskManager(models.Manager):
    def task_validator(self,postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = 'Task must be at least 2 characters'
        if len(postData['desc']) < 3:
            errors['desc'] = 'Description must be at least 3 characters'
        return errors
    def bill_validator(self, postData):
        errors = {}
        if len(postData['collector']) < 2:
            errors['collector'] = 'Bill collector must be at least 2 characters'
        if float(postData['amount']) < 0:
            errors['amount'] = 'How much do we owe?'
        return errors
    def reminder_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = 'Reminder must be at least 2 characters'
        if len(postData['desc']) < 3:
            errors['desc'] = 'Description must be at least 3 characters'
        return errors
        



class Bill(models.Model):
    collector = models.CharField(max_length=255)
    amount = models.FloatField()
    duedate = models.DateField()
    addedby = models.ForeignKey(Tenant, related_name='bills', on_delete=models.CASCADE)
    done = models.CharField(max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TaskManager()

class Task(models.Model):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    addedby = models.ForeignKey(Tenant, related_name='tasks', on_delete=models.CASCADE)
    done = models.CharField(max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TaskManager()

class Reminder(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    date = models.DateTimeField()
    addedby = models.ForeignKey(Tenant, related_name='reminders', on_delete=models.CASCADE)
    done = models.CharField(max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TaskManager()