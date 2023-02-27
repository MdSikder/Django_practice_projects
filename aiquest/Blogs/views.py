from django.shortcuts import render
from django.http import HttpResponse
from .form import TeachersRegistration

# Create your views here.
def Blogs(request):
    return render(request,'blogs/Blogs.html')

def showformsdata(request):
    if request.method == 'POST':
        fm = TeachersRegistration(request.POST)
        if fm.is_valid():

            print(fm.cleaned_data['password'])
            print(fm.cleaned_data['repassword'])
            print('This is POST statement')  
            print(fm.changed_data)
    else:
        fm = TeachersRegistration()
        print('This is GET Statement')
    return render(request, 'blogs/forms.html', {'form': fm})