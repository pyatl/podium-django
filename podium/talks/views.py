from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy
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
    raise Http404(
        'This view is not implemented. Please tell the Podium maintainers to fix this.')


def session_list_view(request):
    sessions = Session.objects.all()
    # sessions = [s.filter(status='A') for s in sessions]
    print(sessions)
    context = {'sessions': sessions}
    return render(request, 'talks/sessions.html', context)


def session_talk_list_view(request, id):
    session = get_object_or_404(Session, id=id)
    return render(request, 'talks/session-detail.html', {
        'session': session,
        'talks': session.talks_available.all(),
    })
