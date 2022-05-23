from django.urls import path
from SignalsApp import views
urlpatterns = [
    path('',views.home),
    path('',views.index),
]