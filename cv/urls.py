from django.urls import path
from . import views

urlpatterns = [
        path('', views.cv1, name='cv1')
]