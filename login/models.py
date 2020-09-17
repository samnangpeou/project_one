from django.db import models

# Create your models here.
class TenantManager(models.Manager):
    def log_validator(self,postData):
        errors = {}
        if len(postData['username']) < 1:
            errors['username'] = 'Enter a username'
        if len(postData['password']) < 1:
            errors['password'] = 'Enter a password'
        return errors


class Tenant(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TenantManager()