from django.shortcuts import render
from django.views import View
from django.conf import settings
from django.http import JsonResponse
from .forms import ResumeForm
from .models import Resume
from pyresparser import ResumeParser
import os


class ResumeUpload(View):
    def get(self, request):
        form = ResumeForm()
        return render(self.request, 'resume/upload.html', {'form': form})

    def post(self, request):
        # form = ResumeForm(self.request.POST, self.request.FILES)
        # files = request.FILES.getlist('file')
        # if form.is_valid():
        #     for file in files:
        #         print(file)
        #         pass
        #     return render(self.request, 'resume/upload.html')
        # else:
        #     return render(self.request, 'resume/upload.html')
        form = ResumeForm(self.request.POST, self.request.FILES)
        files = request.FILES.getlist('file')
        try:
            for file in files:
                resume_file = Resume.objects.filter(name__exact=file.name).exists()
                if form.is_valid() and not resume_file:
                    resume = form.save(commit=False)
                    resume.name = resume.file.name.replace('resume/', '')
                    # resume_path = os.path.join(settings.BASE_DIR, resume.file.url[1:])
                    data = ResumeParser(file.file.name).get_extracted_data()
                    skills = data.get('skills', '')
                    if skills != '':
                        skills = ', '.join(skills)
                    resume.skills = skills
                    resume.save()
                    data = {'is_valid': True, 'name': resume.file.name, 'url': resume.file.url, 'skills': skills}
                elif resume_file:
                    resume = Resume.objects.get(name__exact=file.name)
                    data = {'is_valid': True, 'error': '%s already exists...' % file.name,
                            'name': resume.name, 'url': resume.file.url, 'skills': resume.skills}
                else:
                    data = {'is_valid': False, 'error': 'File not supported. Please upload pdf or docx or doc resumes'}
                return JsonResponse(data)
        except BaseException as e:
            data = {'is_valid': False, 'error': str(e)}
            return JsonResponse(data)
