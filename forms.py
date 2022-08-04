from django import forms
from django.forms import inlineformset_factory
from .models import Project, ProjectNote, Technician

class ProjectForm(forms.ModelForm):
    def __init__(self, **kwargs):
        return super().__init__(**kwargs)

    class Meta:
        model = Project
        fields = [
            'page',
            'slug',
        ]
        widgets = {
            'title':forms.TextInput(attrs={'class':'widthlong'}),
            'description':forms.Textarea(attrs={'class':'widthlong'}),
            'begin':forms.DateTimeInput(format='%Y-%m-%dT%H:%M:%S',  attrs={'type':'datetime-local'} ),

        }


ProjectProjectNoteFormset = inlineformset_factory(Project, ProjectNote, form=ProjectProjectNoteForm, extra=10)
