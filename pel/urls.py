from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("encode/", views.encode, name="encode"),
    path("about/", views.about, name="about"),
    path("decode/", views.decode, name="decode"),
    path('download/', views.download, name='download'),
    # path("download/", views.download, name="download"),
]