from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .models import Submission
from .forms import SubmissionForm


class SubmissionListView(ListView):
    template_name = "submissions/submission_list.html"
    model = Submission

    def get_queryset(self):
        return self.request.user.team_set.first().submission_set.all()


class SubmissionCreateView(CreateView):
    template_name = "submissions/submission_create.html"
    model = Submission
    form_class = SubmissionForm

    def dispatch(self, request, *args, **kwargs):
        if not request.user.submission_set.all().exists():
            msg = "You must be on a team to make a submission."
            messages.warning(request, msg)
            return redirect('submission_list')
        return super(SubmissionCreateView, self).dispatch(request, *args, **kwargs)

    def get_initial(self):
        return {'team': self.request.user.team_set.first()}


submission_list_view = login_required(SubmissionListView.as_view())
submission_create_view = login_required(SubmissionCreateView.as_view())
