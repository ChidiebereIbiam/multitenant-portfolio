from django.shortcuts import render

# Create your views here.

def porfolio(request):
    return render(request, "portfolio/portfolio.html")
