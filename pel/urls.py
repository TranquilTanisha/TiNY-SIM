from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("encode/", views.encode, name="encode"),
<<<<<<< HEAD
=======
    path("download/<str:pk>/", views.download, name="download"),
    path("about/", views.about, name="about"),
>>>>>>> ca40282d48368c1918a1ea3d3e372cea82e114d6
    path("decode/", views.decode, name="decode"),
]