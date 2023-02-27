from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from . import views

# Create your views here.
def data_analysis(request):
    return render(request,'data_analysis/data_analysis.html')

class DataAnalysis(View):
    def get(self,request):
        return render(request,'data_analysis/class.html')