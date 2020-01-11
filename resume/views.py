from django.shortcuts import render
from django.views import View
from django.conf import settings
from django.http import JsonResponse
from .forms import ResumeForm
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
                print(file.name)
            if form.is_valid():
                resume = form.save()
                resume_path = os.path.join(settings.BASE_DIR, resume.file.url[1:])
                data = ResumeParser(resume_path).get_extracted_data()
                skills = data.get('skills', '')
                if skills != '':
                    skills = ', '.join(skills)
                data = {'is_valid': True, 'name': resume.file.name, 'url': resume.file.url, 'skills': skills}
            else:
                data = {'is_valid': False, 'error': 'File not supported. Please upload pdf or docx resumes'}
            return JsonResponse(data)
        except BaseException as e:
            data = {'is_valid': False, 'error': e.__suppress_context__}
            return JsonResponse(data)
