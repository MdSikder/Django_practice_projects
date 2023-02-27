from django.urls import path
from . import views

urlpatterns = [
    path('machine/',views.machine_learning),
    path('rf/',views.random, name="rf"),
    path('knn/',views.k_nearest, name="knn"),
    path('dt/',views.dtree, name = "DT"),
    # path('d4/',views.deep_learning),
    # path('au/',views.about_us),
    # path('cu/',views.contact_us),

]