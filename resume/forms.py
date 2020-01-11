from .models import Resume
from django import forms


class ResumeForm(forms.ModelForm):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Resume
        fields = ('file',)
