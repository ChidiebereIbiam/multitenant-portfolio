from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.porfolio, name="portfolio"),
    path('create_portfolio/<str:step>/', views.create_portfolio, name='create_portfolio'),
    path('create_portfolio/', views.create_portfolio, {'step': 'profile'}, name='create_portfolio_initial'),
    path('profile/', views.profile_view, name='profile'),
    path('service/', views.service_view, name='service'),
    path('education/', views.education_view, name='education'),
    path('work_experience/', views.work_experience_view, name='work_experience'),
    path('project/', views.project_view, name='project'),
    path('contact/', views.contact_view, name='contact'),
    path('skills/', views.skills_view, name='skills'),
    path('success/', views.success_view, name='success'),
    path("project/<id>", views.project_detail, name="project-detail"),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
