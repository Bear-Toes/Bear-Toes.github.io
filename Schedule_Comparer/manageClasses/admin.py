from django.contrib import admin
from .models import Student, Teacher, FSSClass, AfterSchoolActivity

# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(FSSClass)
admin.site.register(AfterSchoolActivity)