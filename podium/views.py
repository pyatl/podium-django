from django.shortcuts import render
<<<<<<< HEAD


def index(request):
    context = {
        'title': 'PyAtl',
        'details': 'In Town - Every second Thurs. of the month.'
    }
    return render(request, 'index.html', context)
=======
from podium.talks.models import Session,Talk


def index (request):
	context ={
		'title':'PyAtl Jam Session',
		'details':'In Town - Every first Thurs. of the month.'
	}
	return render(request, 'index.html', context)
>>>>>>> f6afdd7f38afc2de077ec666921d8c90051396e0
