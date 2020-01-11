from django.contrib import admin
from django.urls import path, include
from .views import ResumeUpload

urlpatterns = [
    path('', ResumeUpload.as_view(), name='resume_upload')
]