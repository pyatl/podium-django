from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse,reverse_lazy
from podium.talks.models import Session,Talk


def index (request):
	context ={
	'title':'PyAtl Jam Session',
	'details':'In Town - Every First Thurs. of the Month'
	}
	return render(request, 'index.html',context)
# def talks(request):
# 	return render(request, 'talks.html' )
# def sessions(request):
# 	return render(request, 'sessions.html')
# def details(request, id):
# 	return render(request, 'details.html')
