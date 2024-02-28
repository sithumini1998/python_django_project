from django.urls import path
from .import views
#urlcinfig
urlpatterns=[
    path('hello/',views.say_hello)
    ]