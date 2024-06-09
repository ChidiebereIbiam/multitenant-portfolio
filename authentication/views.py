from django.shortcuts import redirect, render,get_object_or_404
from django.views import generic
from .forms import SignUpForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group



# Create your views here.
def registerpage(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')

    context = {'form':form}
    return render(request, 'registration/register.html', context)


def create_tenant(request):
    context = {}
    return render(request, 'registration/create_tenant.html', context)

