from django.shortcuts import render
from podium.talks.models import Session,Talk


def index (request):
	context ={
		'title':'PyAtl Jam Session',
		'details':'In Town - Every first Thurs. of the month.'
	}
	return render(request, 'index.html', context)
