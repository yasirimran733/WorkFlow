from django.shortcuts import render ,redirect
from .models import Project
from django.shortcuts import get_object_or_404
from clients.models import *
# Create your views here.

def addProject(request):
    if request.method == 'POST':
        data = request.POST
        user = request.user
        title = data.get('title')
        description = data.get('description')
        budget  = data.get('budget')
        paid = data.get('paid')
        startDate = data.get('startDate')
        deadline = data.get('deadline')
        clientId = data.get('client')
        client = None
        if clientId:
            client = Client.objects.get(id = clientId)
        Project.objects.create(
            user = user,
            title = title,
            description =  description,
            budget = budget,
            paid = paid,
            client = client,
            startDate = startDate,
            deadline = deadline,
        )
        return redirect('projects:showProjects')
    clientData = Client.objects.filter(user = request.user)
    return render(request,'projects/addProject.html',{'clients' : clientData})  

def editProject(request,id):
    project = get_object_or_404(Project,id=id,user=request.user)
    print(project.id)
    if request.method == 'POST':
        data = request.POST
        project.title = data.get('title')
        project.description = data.get('description')
        project.budget  = data.get('budget')
        project.paid = data.get('paid')
        project.startDate = data.get('startDate')
        project.deadline = data.get('deadline')

        project.save()
        
        return redirect('projects:showProjects')
    else:
        print("Not a Post") 
    return render(request,'projects/editProject.html' , {'project':project})  
  
def deleteProject(request,id):
    project = Project.objects.filter(id=id,user=request.user)
    if project:
        project.delete()
        return redirect('projects:showProjects')
    return render(request,'projects/showProjects.html')




def showProjects(request):
    projects = Project.objects.filter(user=request.user)
    return render(request,'projects/showProjects.html' , {'projects': projects})

def searchProject(request):
    if request.method == 'GET':
        data = request.GET
        q = data.get('search')
        projects = Project.objects.filter(user = request.user , title__contains = q)
    return render(request, 'projects/showProjects.html' , {'projects' : projects , 'q' : q})    

def projectDetail(request,id):
    project = Project.objects.get(id=id)
    return render(request,'projects/projectDetail.html',{'project':project})