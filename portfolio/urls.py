from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.porfolio, name="portfolio"),
    path('profile-setup/', views.profile_setup_view, name='profile_setup'),
    path('service-setup/', views.service_setup_view, name='service_setup'),
    path("service-delete/<int:id>", views.delete_service, name="delete-service"),
    path("service-edit/<int:id>", views.edit_service, name="edit-service"),
    path('education/', views.education_view, name='education'),
    path('work_experience/', views.work_experience_view, name='work_experience'),
    path('project/', views.project_view, name='project'),
    path('contact-setup/', views.contact_setup_view, name='contact_setup'),
    path('skills/', views.skills_view, name='skills'),
    path("project/<id>", views.project_detail, name="project-detail"),
    path('portfolio-setup/', views.portfolio_setup, name='portfolio_setup'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
