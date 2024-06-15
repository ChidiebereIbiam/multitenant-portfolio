from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerpage, name="register"),
    path('create-tenant/', views.create_tenant, name="create_tenant"),
    path('list-tenant/', views.list_tenant, name="list_tenant"),
]
