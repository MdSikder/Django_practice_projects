from django.urls import path
from . import views

urlpatterns = [

    path('blo/', views.Blogs, name="blog"),
    path('fm/', views.showformsdata),
    # path('fm/', views.showformsdata),
    #

]
