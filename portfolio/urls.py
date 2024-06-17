from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from authentication.views import login_view

urlpatterns = [
    path("", views.porfolio, name="portfolio"),
    path('profile-setup/', views.profile_setup_view, name='profile_setup'),
    path('service-setup/', views.service_setup_view, name='service_setup'),
    path("service-delete/<int:id>", views.delete_service, name="delete-service"),
    path("service-edit/<int:id>", views.edit_service, name="edit-service"),
    
    path('education-setup/', views.education_setup_view, name='education_setup'),
    path("education-delete/<int:id>", views.delete_education, name="delete-education"),
    path("education-edit/<int:id>", views.edit_education, name="edit-education"),
    
    path('work-experience-setup/', views.work_experience_setup_view, name='work_experience_setup'),
    path("work-experience-delete/<int:id>", views.delete_work_experience, name="delete-work-experience"),
    path("work-experience-edit/<int:id>", views.edit_work_experience, name="edit-work-experience"),

    path('project-setup/', views.project_setup_view, name='project_setup'),
    path("project-delete/<int:id>", views.delete_project, name="delete-project"),
    path("project-edit/<int:id>", views.edit_project, name="edit-project"),

    path('contact-setup/', views.contact_setup_view, name='contact_setup'),

    path('skills-setup/', views.skills_setup_view, name='skills_setup'),
    path("skills-delete/<int:id>", views.delete_skills, name="delete-skills"),
    path("skills-edit/<int:id>", views.edit_skills, name="edit-skills"),

    path("project/<id>", views.project_detail, name="project-detail"),
    path('portfolio-setup/', views.portfolio_setup, name='portfolio_setup'),

    path('authentication/login/', login_view, name="login"),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)






    