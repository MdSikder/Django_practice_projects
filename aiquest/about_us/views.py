from django.shortcuts import render
from django.http import HttpResponse
from about_us.models import Teacher
# Create your views here.
def Blogs(request):
    return render(request,'about/about.html')

def teachers_info(request):
    teach = Teacher.objects.all()
    return render (request, 'about/teacher.html', {'thr': teach})
