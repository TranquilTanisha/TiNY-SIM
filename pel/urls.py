from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("encode/", views.encode, name="encode"),
    path("download/<str:pk>/", views.download, name="download"),
    path("about/", views.about, name="about"),
    path("decode/", views.decode, name="decode"),
]