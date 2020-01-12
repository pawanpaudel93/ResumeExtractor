from django.contrib import admin
from django.urls import path, include
from .views import ResumeUpload, DisplayResume

urlpatterns = [
    path('', ResumeUpload.as_view(), name='resume_upload'),
    path('resumes/', DisplayResume.as_view(), name='display_resume')
]