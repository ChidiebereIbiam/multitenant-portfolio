from django.shortcuts import render, redirect
from .forms import (ProfileForm, 
                    ServiceForm, 
                    EducationForm, 
                    WorkExperienceForm, 
                    ProjectForm, 
                    ContactForm, 
                    SkillsForm)
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



def create_portfolio(request, step='profile'):
    forms = {
        'profile': ProfileForm,
        'service': ServiceForm,
        'education': EducationForm,
        'work_experience': WorkExperienceForm,
        'project': ProjectForm,
        'contact': ContactForm,
        'skills': SkillsForm,
    }
    
    if step not in forms:
        step = 'profile'
    
    if request.method == 'POST':
        form = forms[step](request.POST, request.FILES)
        if form.is_valid():
            form.save()
            next_step = request.POST.get('next_step')
            if 'save_add_another' in request.POST:
                return redirect(f'/create_portfolio/{step}')
            return redirect(f'/create_portfolio/{next_step}')
    else:
        form = forms[step]()
    
    return render(request, 'portfolio/progressive_form.html', {'form': form, 'step': step})


def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('service')
    else:
        form = ProfileForm()
    return render(request, 'portfolio/progressive_form.html', {'form': form, 'step': 'profile'})

def service_view(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            if 'save_add_another' in request.POST:
                return redirect('service')
            return redirect('education')
    else:
        form = ServiceForm()
    return render(request, 'portfolio/progressive_form.html', {'form': form, 'step': 'service'})

def education_view(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            form.save()
            if 'save_add_another' in request.POST:
                return redirect('education')
            return redirect('work_experience')
    else:
        form = EducationForm()
    return render(request, 'portfolio/progressive_form.html', {'form': form, 'step': 'education'})

def work_experience_view(request):
    if request.method == 'POST':
        form = WorkExperienceForm(request.POST)
        if form.is_valid():
            form.save()
            if 'save_add_another' in request.POST:
                return redirect('work_experience')
            return redirect('project')
    else:
        form = WorkExperienceForm()
    return render(request, 'portfolio/progressive_form.html', {'form': form, 'step': 'work_experience'})

def project_view(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            if 'save_add_another' in request.POST:
                return redirect('project')
            return redirect('contact')
    else:
        form = ProjectForm()
    return render(request, 'portfolio/progressive_form.html', {'form': form, 'step': 'project'})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            if 'save_add_another' in request.POST:
                return redirect('contact')
            return redirect('skills')
    else:
        form = ContactForm()
    return render(request, 'portfolio/progressive_form.html', {'form': form, 'step': 'contact'})

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

def success_view(request):
    return render(request, 'success.html')



def project_detail(request, id):
    project = Project.objects.get(id = id)
    return render(request, "portfolio/project-detail.html", {"project":project})