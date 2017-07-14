from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from .forms import TalkSubmissionForm
from .models import Session


def submit_talk_view(request):
    form = TalkSubmissionForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TalkSubmissionForm()
        return HttpResponseRedirect(reverse_lazy('talks-sessions'))
    return render(request, 'talks/submit.html', {
        'form': form,
    })


def talk_detail_view(request, talk_id):
    pass


def session_list_view(request):
    sessions = Session.objects.all()
    context = {'sessions': sessions}
    return render(request, 'talks/sessions.html', context)


def session_talk_list_view(request):
    pass
