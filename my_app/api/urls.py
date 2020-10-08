from django.urls import path
from api import views

urlpatterns = [
    path('', views.json_images, name=None)
]
