from django.shortcuts import get_object_or_404, render, redirect
from .forms import (ProfileForm, ServiceForm, EducationForm, WorkExperienceForm, 
                    ProjectForm, ContactForm, SkillsForm)
from .models import Profile, Service, Education, WorkExperience, Project, Contact, Skills


def porfolio(request):
    profile = Profile.objects.first() or None
    if profile:
        service = Service.objects.all()
        education = Education.objects.all().order_by('-id')
        experience = WorkExperience.objects.all().order_by('-id')
        skill1 = Skills.objects.all()[0:3]
        skill2 = Skills.objects.all()[3:6]
        contact = Contact.objects.first() or None
        project = Project.objects.all().order_by('-id')
        project_count = Project.objects.all().count()

        context = {
            'profile': profile,
            'services': service,
            'educations':education,
            'experiences':experience,
            "skill1":skill1,
            "skill2":skill2,
            "contact":contact,
            'projects':project,
            'project_count': project_count,
        }

        return render(request, "portfolio/portfolio.html", context)
    else:
        return render(request, "portfolio/no_portfolio.html")



def skills_view(request):
    if request.method == 'POST':
        form = SkillsForm(request.POST)
        if form.is_valid():
            form.save()
            if 'save_add_another' in request.POST:
                return redirect('skills')
            return redirect('success')
    else:
        form = SkillsForm()
    return render(request, 'portfolio/progressive_form.html', {'form': form, 'step': 'skills'})


def project_detail(request, id):
    project = Project.objects.get(id = id)
    return render(request, "portfolio/project-detail.html", {"project":project})


def portfolio_setup(request):
    profile = Profile.objects.first() or None
    if profile:
        context = {
                'profile': profile,
            }
        return render(request, "portfolio/porfolio-setup.html", context)
    else:
        form = ProfileForm()
        return render(request, 'portfolio/profile-setup.html', {'form': form})


def profile_setup_view(request):
    profile = Profile.objects.first() or None
    if request.method == 'POST':
        if profile:
            form = ProfileForm(request.POST, request.FILES, instance=profile)
        else:
            form = ProfileForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('service_setup')
    else:
        if profile:
            form = ProfileForm(instance=profile)
        else:
            form = ProfileForm()
    return render(request, 'portfolio/profile-setup.html', {'form': form})

def service_setup_view(request):
    services = Service.objects.all()
    form = ServiceForm()

    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_setup')
        
    return render(request, 'portfolio/service-setup.html', {'form': form, 'services': services})


def delete_service(request, id):
    service = get_object_or_404(Service, id=id)
    service.delete()
    return redirect("service_setup")

def edit_service(request, id):
    service = get_object_or_404(Service, id=id)
    
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service_setup')
    else:
        form = ServiceForm(instance=service)
    
    context =  {
        'form': form, 
        'services': Service.objects.all(), 
        'edit_service': service
    }
    return render(request, 'portfolio/service-setup.html', context)

def education_setup_view(request):
    educations = Education.objects.all()
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('education_setup')
    else:
        form = EducationForm()
    return render(request, 'portfolio/education-setup.html', {'form': form, 'educations': educations})

def delete_education(request, id):
    education = get_object_or_404(Education, id=id)
    education.delete()
    return redirect("education_setup")

def edit_education(request, id):
    education = get_object_or_404(Education, id=id)
    
    if request.method == 'POST':
        form = EducationForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            return redirect('education_setup')
    else:
        form = EducationForm(instance=education)
    
    context = {
        'form': form, 
        'educations': Education.objects.all(), 
        'edit_education': education
        }

    return render(request, 'portfolio/education-setup.html', context)

def work_experience_setup_view(request):
    work_experiences = WorkExperience.objects.all()
    if request.method == 'POST':
        form = WorkExperienceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('work_experience_setup')
    else:
        form = WorkExperienceForm()
    return render(request, 'portfolio/work-experience-setup.html', {'form': form, 'work_experiences': work_experiences})


def delete_work_experience(request, id):
    work_experiences = get_object_or_404(WorkExperience, id=id)
    work_experiences.delete()
    return redirect("work_experience_setup")


def edit_work_experience(request, id):
    work_experience = get_object_or_404(WorkExperience, id=id)
    
    if request.method == 'POST':
        form = WorkExperienceForm(request.POST, instance=work_experience)
        if form.is_valid():
            form.save()
            return redirect('work_experience_setup')
    else:
        form = WorkExperienceForm(instance=work_experience)
    
    context = {
        'form': form, 
        'work_experiences': WorkExperience.objects.all(), 
        'edit_work_experience': work_experience
        }

    return render(request, 'portfolio/work-experience-setup.html', context)

def project_setup_view(request):
    projects = Project.objects.all()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('project_setup')
    else:
        form = ProjectForm()
    return render(request, 'portfolio/project-setup.html', {'form': form, 'projects': projects})

def delete_project(request, id):
    project = get_object_or_404(Project, id=id)
    project.delete()
    return redirect("project_setup")


def edit_project(request, id):
    project = get_object_or_404(Project, id=id)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_setup')
    else:
        form = ProjectForm(instance=project)
    
    context = {
        'form': form, 
        'projects': Project.objects.all(), 
        'edit_project': project
        }

    return render(request, 'portfolio/project-setup.html', context)

def contact_setup_view(request):
    contact = Contact.objects.first() or None
    if request.method == 'POST':
        if contact:
            form = ContactForm(request.POST, instance=contact)
        else:
            form = ContactForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('portfolio_setup')
    else:
        if contact:
            form = ContactForm(instance=contact)
        else:
            form = ContactForm()
    return render(request, 'portfolio/contact-setup.html', {'form': form})