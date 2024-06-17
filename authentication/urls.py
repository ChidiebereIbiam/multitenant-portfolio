from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerpage, name="register"),
    path('login/', views.login_view, name="login"),
    path('create-tenant/', views.create_tenant, name="create_tenant"),
    path('list-tenant/', views.list_tenant, name="list_tenant"),
]
