# forms.py
from django import forms
from .models import Profile, Service, Education, WorkExperience, Project, Contact, Skills

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = '__all__'

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = '__all__'
