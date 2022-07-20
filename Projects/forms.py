from django.forms import ModelForm, widgets
from .models import Project
from django import forms

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["title","featured_image", "description", "demo_link", "source_link", "tags"]

        widgets = {
            "tags": forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kargs):
        super(ProjectForm, self).__init__(*args, **kargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({"class": "input"})
        
        #self.fields["title"].widget.attrs.update({"class": "input", "placeholder": "Add Title"})
        #self.fields["description"].widget.attrs.update({"class": "input", "placeholder": "Description"})
