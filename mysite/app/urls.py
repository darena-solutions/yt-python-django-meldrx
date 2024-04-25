from django.urls import path

from . import views

urlpatterns = [
    path("home", views.home, name="home"),
    path("get", views.get_patient, name="get_patient"),
    path("create", views.create_patient, name="create_patient"),
]
