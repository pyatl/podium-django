from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import TalkSubmissionForm
from .models import Session, Talk

NOT_IMPLEMENTED_MSG = 'This view is not implemented. Please tell the Podium ' \
                      'maintainers to fix this.'


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
    talk = get_object_or_404(Talk, id=talk_id)
    context = {
        'talk': talk,
    }
    return render(request, 'talks/talk_detail.html', context)


def talk_list_view(request):
    talks = Talk.objects.all()
    context = {
        'talks': talks,
    }
    return render(request, 'talks/talks.html', context)


def session_list_view(request):
    sessions = Session.objects.all()
    context = {'sessions': sessions}
    return render(request, 'talks/sessions.html', context)


def session_talk_list_view(request, id):
    session = get_object_or_404(Session, id=id)
    return render(request, 'talks/session-detail.html', {
        'session': session,
        'talks': session.talks_available.all(),
    })
