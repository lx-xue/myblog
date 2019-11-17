from django.urls import path
from blog import views

urlpatterns = [
    path('index/', views.index),
    path('article/<article_id>/', views.article_page),
    path('add/', views.add_page),
    path('add/action/', views.add_action),
    path('edit/<article_id>/', views.edit_page),
    path('edit_action/', views.edit_action),
]
