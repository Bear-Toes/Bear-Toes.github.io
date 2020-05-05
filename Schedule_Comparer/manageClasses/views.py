from django.shortcuts import render
from django.http import Http404
from .models import Student, Teacher, FSSClass, AfterSchoolActivity

# Create your views here.
def index(request):
    all_students = Student.objects.all()
    return render(request, 'manageClasses/index.html', {'all_students': all_students})

def detail(request, name):
    try:
        stud = Student.objects.get(name=name)
    except stud.DoesNotExist:
        raise Http404("Student Does Not Exist")
    return render(request, 'manageClasses/detail.html', {'student': stud})