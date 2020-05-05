from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Teacher, FSSClass, AfterSchoolActivity

# Create your views here.
def index(request):
    all_students = Student.objects.all()
    context = {
        'all_students': all_students,
    }
    return render(request, 'manageClasses/index.html', context)

def detail(request, name):
    print("I tried to render")
    return HttpResponse("<h1>This is the page all about the student named " + str(name) + ".</h1>")