from django.urls import path
from . import views

urlpatterns = [

    path('d2/',views.deep_learning, name = "deep"),
    path('register/',views.registration)

]