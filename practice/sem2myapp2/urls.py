from django.urls import path
from . import views

urlpatterns = [
    path('author/', views.author_read, name='author'),
]