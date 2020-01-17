from django.shortcuts import render
from django.views import View, generic
from django.http import JsonResponse
from .forms import ResumeForm
from .models import Resume
from pyresparser import ResumeParser
import time


class ResumeUpload(View):
    def get(self, request):
        form = ResumeForm()
        return render(self.request, 'resume/upload.html', {'form': form})

    def post(self, request):
        form = ResumeForm(self.request.POST, self.request.FILES)
        files = request.FILES.getlist('file')
        for file in files:
            start_time = time.time()
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
                elapsed_time = time.time() - start_time
                elapsed_time = "%.2f" % elapsed_time
                if elapsed_time == 'undefined':
                    elapsed_time = 0
                data = {'is_valid': True, 'name': resume.name, 'url': resume.file.url,
                        'skills': skills, 'time': elapsed_time}

            elif form.is_valid() and resume_file:
                elapsed_time = time.time() - start_time
                elapsed_time = "%.2f" % elapsed_time
                if elapsed_time == 'undefined':
                    elapsed_time = 0
                resume = Resume.objects.get(name__exact=file.name)
                data = {'is_valid': True, 'error': '%s already exists...' % file.name,
                        'name': resume.name, 'url': resume.file.url, 'skills': resume.skills, 'time': elapsed_time}

            else:
                data = {'is_valid': False, 'error': 'File not supported. Please upload pdf or docx or doc resumes'}
            return JsonResponse(data)


class DisplayResume(generic.ListView):
    template_name = 'resume/skills.html'
    context_object_name = 'resumes'

    def get_queryset(self):
        return Resume.objects.all()
