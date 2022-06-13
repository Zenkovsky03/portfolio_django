from email.quoprimime import body_check
from multiprocessing import context
from django.shortcuts import render
from .models import Project, Skill
# Create your views here.

def homePage(request):
  projects = Project.objects.all()
  skills = Skill.objects.filter(body = '') #zawiera pusty opis
  detailedSkills = Skill.objects.exclude(body = '') #wyklucza pusty opis
  context = {'projects':projects, 'skills':skills, 'detailedSkills': detailedSkills}
  return render(request, 'base/home.html', context)

def projectPage(request, pk):
  project = Project.objects.get(id=pk)
  context = {'project':project}
  return render(request, 'base/project.html', context)