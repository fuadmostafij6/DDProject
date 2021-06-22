from django.db import models
from django.contrib.auth.models import User


class AdminProfile(models.Model):
    adminuser = models.OneToOneField(User, on_delete=models.CASCADE, default='admin')
    image = models.ImageField(upload_to="profile/", blank=True, null=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    personal_details = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.adminuser.username


class Dep(models.Model):
    dept_name = models.CharField(max_length=100, default='')
    def __str__(self):
        return self.dept_name

class Sec(models.Model):
    sec_name = models.CharField(max_length=100, default='')
    def __str__(self):
        return self.sec_name


class TeacherProfile(models.Model):
    username = models.CharField(max_length=100, default='teacher')
    password = models.CharField(max_length=50, default='1234')
    dept_name = models.CharField(max_length=10,default='CSE')
    

    def __str__(self):
        return self.username
class StudentProfile(models.Model):
    username = models.CharField(max_length=100, default='students')
    password = models.CharField(max_length=50, default='12345678')
    dept_name = models.ForeignKey(Dep, on_delete=models.CASCADE)
    sec_name = models.ForeignKey(Sec, on_delete=models.CASCADE)

    def __str__(self):
       return self.username

        