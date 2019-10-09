from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return render(request,'home/index.html')
def projects(request):
	return render(request,'home/projects.html')
def team(request):
	return render(request,'home/team.html')
def home(request):
	return render(request,'home/index.html')