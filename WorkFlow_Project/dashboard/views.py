from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from projects.models import Project
from clients.models import Client
from accounts.models import Profile
# Create your views here.

def home(request):
    return render(request , 'dashboard/home.html')

@login_required
def dashboard(request):
    projectCount = Project.objects.filter(user = request.user).count()
    clientCount = Client.objects.filter(user = request.user).count()
    projects = Project.objects.filter(user = request.user)
    totalAmount = 0
    totalPaid = 0
    for p in projects:
        totalAmount = totalAmount + p.budget
        totalPaid=totalPaid + p.paid
    remainingAmount = totalAmount - totalPaid
    context = {
        'username' : request.user,
        'projectCount' : projectCount,
        'clientCount' : clientCount,
        'totalAmount':totalAmount,
        'totalPaid':totalPaid,
        'remainingAmount' : remainingAmount,
    }
    return render(request , 'dashboard/dashboard.html', context=context)

def about(request):
    return render(request , 'dashboard/about.html')

def contact(request):
    return render(request , 'dashboard/contact.html')
    
@login_required    
def myProfile(request):
    profile = Profile.objects.get(user = request.user)
    print(profile)
    return render(request,'dashboard/myprofile.html' , {'profile' : profile})