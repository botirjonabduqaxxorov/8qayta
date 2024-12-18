from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('add_course/', views.add_course, name='add_course'),
    path('add_lesson/', views.add_lesson, name='add_lesson'),
]
