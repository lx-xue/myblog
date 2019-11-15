from django.urls import path
from blog2 import views
urlpatterns = [
    path('', views.index),
]