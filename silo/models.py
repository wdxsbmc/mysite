from django.db import models
from django.contrib import admin

# Create your models here.
class silo_data(models.Model):
    iAutoId = models.AutoField(primary_key=True,default=None)
    info = models.CharField(max_length=256,default=None)

class  User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(default="")

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','password','email')

admin.site.register(User,UserAdmin)
