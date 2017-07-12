from django.shortcuts import render, redirect

from .forms import TalkSubmissionForm


def submit_talk_view(request):
    form = TalkSubmissionForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TalkSubmissionForm()
        return HttpResponseRedirect(reverse_lazy('sessions',))
    return render(request, 'talks/submit.html', {
        'form': form,
    })


def talk_detail_view(request, talk_id):
    pass


def session_list_view(request):
    
     sessions = Session.objects.all()
     context = {
                'sessions':sessions
     }
     return render(request, 'talks/session.html', context)


def session_talk_list_view(request):
    pass
