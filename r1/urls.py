from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('studentinfo/<int:pk>',views.student_info),
    path('studentinfo/',views.student),
]