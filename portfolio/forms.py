# forms.py
from django import forms
from .models import Profile, Service, Education, WorkExperience, Project, Contact, Skills

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("first_name", "middle_name","last_name", "location", "about_me", "email", "role",
                  "profile_photo", "cv", "years_of_experience", "happy_clients", "github", "facebook",
                  "twitter", "linkedin")

        widgets = {
                'first_name': forms.TextInput(attrs={'class':'form-control'}),
                'middle_name': forms.TextInput(attrs={'class':'form-control'}),
                'last_name': forms.TextInput(attrs={'class':'form-control'}),
                'location':forms.TextInput(attrs={'class':'form-control'}),
                'about_me': forms.Textarea(attrs={'class':'form-control', 'rows':'2'}),
                'email':forms.EmailInput(attrs={'class':'form-control'}),
                'role':forms.TextInput(attrs={'class':'form-control'}),
                'profile_photo':forms.FileInput(attrs={'class':'form-control'}),
                'cv':forms.FileInput(attrs={'class':'form-control'}),
                'years_of_experience':forms.TextInput(attrs={'class':'form-control'}),
                'happy_clients':forms.TextInput(attrs={'class':'form-control'}),
                'github':forms.TextInput(attrs={'class':'form-control'}),
                'facebook':forms.TextInput(attrs={'class':'form-control'}),
                'twitter':forms.TextInput(attrs={'class':'form-control'}),
                'linkedin':forms.TextInput(attrs={'class':'form-control'}),
                
                
            }

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ("name", "description")

        widgets = {
                'name':forms.TextInput(attrs={'class':'form-control'}),
                'description':forms.TextInput(attrs={'class':'form-control'}),       
        }

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ("school","degree","field_of_study","start_date","end_date","description")

        widgets = {
                'school':forms.TextInput(attrs={'class':'form-control'}),
                'degree':forms.TextInput(attrs={'class':'form-control'}),
                'field_of_study':forms.TextInput(attrs={'class':'form-control'}),
                'start_date': forms.widgets.DateInput(
                    format="%m/%d/%Y",
                    attrs={
                        'class':'form-control datetimepicker-input',
                        'data-target': '#datetimepicker1'}),
                'end_date': forms.widgets.DateInput(
                    format="%m/%d/%Y",
                    attrs={
                        'class':'form-control datetimepicker-input',
                        'data-target': '#datetimepicker1'}),
                'description': forms.Textarea(attrs={'class':'form-control', 'rows':'2'}),       
        }


class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ("title","company_name","start_date","end_date","current_job","description")
        
        widgets = {
                'title':forms.TextInput(attrs={'class':'form-control'}),
                'company_name':forms.TextInput(attrs={'class':'form-control'}),
                'start_date': forms.widgets.DateInput(
                    format="%m/%d/%Y",
                    attrs={
                        'class':'form-control datetimepicker-input',
                        'data-target': '#datetimepicker1'}),
                'end_date': forms.widgets.DateInput(
                    format="%m/%d/%Y",
                    attrs={
                        'class':'form-control datetimepicker-input',
                        'data-target': '#datetimepicker1'}),
                'current_job': forms.CheckboxInput(attrs={'class':'form-check-input'}),
                'description': forms.Textarea(attrs={'class':'form-control', 'rows':'2'}),       
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ("title","project_info","client","industry","technology","date", "url",
                  "image1", "image2", "image3")
        
        widgets = {
                'title':forms.TextInput(attrs={'class':'form-control'}),
                'project_info': forms.Textarea(attrs={'class':'form-control', 'rows':'2'}),  
                'client':forms.TextInput(attrs={'class':'form-control'}),
                'industry':forms.TextInput(attrs={'class':'form-control'}),
                'technology':forms.TextInput(attrs={'class':'form-control'}),
                'date': forms.widgets.DateInput(
                    format="%m/%d/%Y",
                    attrs={
                        'class':'form-control datetimepicker-input',
                        'data-target': '#datetimepicker1'}),
                'url':forms.TextInput(attrs={'class':'form-control'}),
                'image1':forms.FileInput(attrs={'class':'form-control'}),
                'image2':forms.FileInput(attrs={'class':'form-control'}), 
                'image3':forms.FileInput(attrs={'class':'form-control'}),      
        }
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("address","phone1","phone2","email")
    
        widgets = {
                'address': forms.Textarea(attrs={'class':'form-control', 'rows':'2'}),
                'email':forms.EmailInput(attrs={'class':'form-control'}),
                'phone1':forms.TextInput(attrs={'class':'form-control'}),
                'phone2':forms.TextInput(attrs={'class':'form-control'}),
                
                
            }

class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ("name","level_of_expertise",)
        widgets = {
                'name':forms.TextInput(attrs={'class':'form-control'}),
                'level_of_expertise':forms.TextInput(attrs={'class':'form-control'}),
                
                
            }

        