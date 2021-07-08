from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model


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
class TecherMainProfile(models.Model):
    username = models.OneToOneField(TeacherProfile, on_delete=models.CASCADE, default='Teacher')
    image = models.ImageField(upload_to="profile/", blank=True, null=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    qualifications = models.CharField(max_length=500, null=True, blank=True)
    reaserch_detail = models.CharField(max_length=1000, blank=True, null=True)

    

    def __str__(self):
        return self.username.username

   

class StudentProfile(models.Model):
    username = models.CharField(max_length=100, default='students')
    password = models.CharField(max_length=50, default='1234',)
    dept_name = models.CharField(max_length=50, default='')
    sec_name = models.CharField(max_length=100, default='')

    def __str__(self):
       return self.username

class StudentsMainProfile(models.Model):
    username = models.OneToOneField(StudentProfile,on_delete=models.CASCADE)
    image = image = models.ImageField(upload_to="profile/", blank=True, null=True)
    email = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.username


class Attendencemodel(models.Model):
    name = models.CharField(max_length=100, null=True, blank= True)
    day = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    attendence = models.CharField(default='0', max_length=10)

    def __str__(self):
        return f'{self.name}--{self.attendence}'


class StudentEvulate(models.Model):
    teacher_name = models.CharField(max_length=100, default='')
    student_name = models.CharField(max_length=100, default='')
    evulotion = models.CharField(max_length=5000, default='')

    def __str__(self):
        return f'teacher_name: {self.teacher_name}--students_name: {self.student_name}'



class TeacherEvulate(models.Model):
    student_name = models.CharField(max_length=100, default='')
    teacher_name = models.CharField(max_length=100, default='')
    
    evulotion = models.CharField(max_length=5000, default='')

    def __str__(self):
        return f'students_name: {self.student_name} --teacher_name: {self.teacher_name}'