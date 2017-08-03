from django.shortcuts import render


def index(request):
    context = {
        'title': 'PyAtl',
        'details': 'In Town - Every second Thurs. of the month.'
    }
    return render(request, 'index.html', context)
