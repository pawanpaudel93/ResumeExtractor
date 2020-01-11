from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .forms import ResumeForm


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
        for file in files:
            print(file)
            pass
        if form.is_valid():
            resume = form.save()
            data = {'is_valid': True, 'name': resume.file.name, 'url': resume.file.path}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)