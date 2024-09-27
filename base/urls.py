#base
from django.contrib import admin
from django.urls import path
from base import views

urlpatterns = [
    path('/',  (views.index)),
    path('register/', (views.register)),
    path('login/',  (views.MyTokenObtainPairSerializer.as_view())),


]
