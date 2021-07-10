from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import EmailField
from django.db.models.fields.related import ForeignKey

# Create your models here.


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    full_name = models.CharField(max_length=200)
    college = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField(null=True)
    photo = models.ImageField(upload_to="Photo")
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Theme(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class College_Event(models.Model):
    STATUS = (('active', 'active'), ('completed', 'completed'))
    TYPE = (('UG', 'UG'), ('PG', 'PG'), ('Engineering',
            'Engineering'), ('diploma', 'diploma'))

    event_name = models.CharField(max_length=200)
    event_date = models.DateField(max_length=200)
    Theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True)
    banner = models.ImageField(upload_to="event_images")
    status = models.CharField(max_length=200, choices=STATUS)
    college = models.CharField(max_length=200, null=True)
    college_type = models.CharField(max_length=200, choices=TYPE,default='none')
    
    description = models.TextField()

    def __str__(self):
        return self.event_name


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Program(models.Model):
    STATUS = (('pending', 'pending'), ('completed', 'completed'))
    event_name = models.ForeignKey(
        College_Event, on_delete=models.CASCADE)
    prg_name = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    start_time = models.TimeField(max_length=200)
    end_time = models.TimeField(max_length=200)
    image = models.ImageField(upload_to="prg_images")
    description = models.TextField()
    max_guest = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    status = models.CharField(max_length=200, choices=STATUS)

    def __str__(self):
        return self.prg_name


class Enroll(models.Model):
    STATUS = (('active', 'active'), ('completed', 'completed'))
    student = models.ForeignKey(
        Student, null=True, on_delete=models.DO_NOTHING)
    event = models.ForeignKey(College_Event, null=True,
                              on_delete=models.DO_NOTHING)
    program = models.ForeignKey(
        Program, null=True, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.event.ename
