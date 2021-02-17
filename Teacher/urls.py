from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import index, TeacherDetailView, TeacherListView


urlpatterns = [
    path('<int:pk>', TeacherDetailView.as_view(), name='teacher_detail'),
    path('', TeacherListView.as_view(), name='teacher_list'),
]



