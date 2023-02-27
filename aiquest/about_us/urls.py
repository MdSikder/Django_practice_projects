from django.urls import path
from . import views

urlpatterns = [

    path('a/',views.Blogs, name='about'),
    path('t/',views.teachers_info)


]