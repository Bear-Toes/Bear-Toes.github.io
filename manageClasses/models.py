from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    
class FSSClass(models.Model):
    name = models.CharField(max_length=250)
    abbr = models.CharField(max_length=10)
    block = models.CharField(max_length=10)
    room = models.CharField(max_length=10)
    students = models.ManyToManyField(Student)
    teachers = models.ManyToManyField(Teacher)

    def __str__(self):
        return self.name

class AfterSchoolActivity(models.Model):
    name = models.CharField(max_length=250)
    students = models.ManyToManyField(Student)
    teachers = models.ManyToManyField(Teacher)

    def __str__(self):
        return self.name