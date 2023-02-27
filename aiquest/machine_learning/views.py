from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def machine_learning(request):
    course = 'machine learning'
    Tclass = 21
    seat = 20
    cduration = '2.5 months'
    offering = {"c" : course, "tl" : Tclass, "st" : seat, "cd" : cduration}
    return render(request,'machine_learning/machine_learing.html', context=offering)

def random(request):
    return render(request,'machine_learning/random_forest.html')

def k_nearest(request):
    return render(request,'machine_learning/knn.html')

def dtree(request):
    return render(request,'machine_learning/DT.html')
# def deep_learning(request):
#     return HttpResponse('<h1>study mart offering a lot of deep learning free & paid course <h1>')

# def about_us(request):
#     return HttpResponse('<h1>we area service provider <h1>')
    
# def contact_us(request):
#     return HttpResponse('<h1>test@gmail.com<h1>')