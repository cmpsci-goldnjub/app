from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.views.generic import View, TemplateView
from django.views.generic.edit import CreateView
from .models import FileSubmission, VideoSubmission
from .forms import FileSubmissionForm, VideoSubmissionForm


class RequiresTeamMixin(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.team_set.all().exists():
            msg = "You must be on a team to make a submission."
            messages.warning(request, msg)
            return redirect('team_list')
        self.team = self.request.user.team_set.first()
        return super(RequiresTeamMixin, self).dispatch(request, *args, **kwargs)


class SubmissionCreateView(RequiresTeamMixin, CreateView):
    template_name = "submission/submission_create.html"

    def get_initial(self):
        return {'team': self.team}

    def form_valid(self, form):
        submission = form.save(commit=False)
        submission.team = self.team
        submission.submitter = self.request.user
        submission.save()

        for member in self.team.members.all():
            subject = 'New H4H submission!'
            message = render_to_string("submission/submission_email.txt",
                                       context={'submission': submission,
                                                'recipient': member})

            send_mail(subject, message, settings.EMAIL_HOST_USER,
                      [member.email], fail_silently=False)

        return redirect('submission_list')


class SubmissionListView(RequiresTeamMixin, TemplateView):
    template_name = "submission/submission_list.html"

    def get_context_data(self, **kwargs):
        context = super(SubmissionListView, self).get_context_data(**kwargs)
        context['team'] = self.team
        return context


class FileSubmissionCreateView(SubmissionCreateView):
    model = FileSubmission
    form_class = FileSubmissionForm


class VideoSubmissionCreateView(SubmissionCreateView):
    model = VideoSubmission
    form_class = VideoSubmissionForm


submission_list_view = login_required(SubmissionListView.as_view())
submission_submit_file = login_required(FileSubmissionCreateView.as_view())
submission_submit_video = login_required(VideoSubmissionCreateView.as_view())
