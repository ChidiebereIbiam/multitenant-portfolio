from django.shortcuts import redirect, render,get_object_or_404
from .forms import SignUpForm, ClientForm
from django.contrib.auth.models import User
from tenant.models import Domain, Client





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
    form = ClientForm()
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            
            tenant = form.save(commit=False)
            tenant.user = request.user
            tenant.save()

            schema_name = form.cleaned_data.get('schema_name')

            domain = Domain()
            domain.domain = f'{schema_name}.localhost'
            domain.tenant = tenant
            domain.is_primary = True
            domain.save()

            return redirect('home')

    context = {'form':form}
    return render(request, 'registration/create_tenant.html', context)

def list_tenant(request):
    tenants = Client.objects.filter(user=request.user)
    context = {'tenants':tenants}
    return render(request, 'registration/list_tenant.html', context)
