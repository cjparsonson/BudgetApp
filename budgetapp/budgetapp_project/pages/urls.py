# urls for the pages routing

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
]
