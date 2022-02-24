from django.urls import path
from uweflix import views

urlpatterns = [
    path("", views.home, name="home"),
    path("viewings/", views.viewings, name="viewings")
]