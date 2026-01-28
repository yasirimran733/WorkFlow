from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from projects.models import Project
from clients.models import Client
# Create your views here.

def home(request):
    return render(request , 'dashboard/home.html')

@login_required
def dashboard(request):
    projectCount = Project.objects.filter(user = request.user).count()
    clientCount = Client.objects.filter(user = request.user).count()
    context = {
        'username' : request.user,
        'projectCount' : projectCount,
        'clientCount' : clientCount,
    }
    return render(request , 'dashboard/dashboard.html', context=context)

def about(request):
    return render(request , 'dashboard/about.html')

def contact(request):
    return render(request , 'dashboard/contact.html')
    
