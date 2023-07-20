from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("encode/", views.encode, name="encode"),
    path("decode/", views.decode, name="decode"),
] 