from django.urls import path
from . import views

urlpatterns = [
    path("", views.porfolio, name="portfolio")
]
