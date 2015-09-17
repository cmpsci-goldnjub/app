from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, get_object_or_404
from django.template.loader import render_to_string
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Team, Request, TeamFullException
from .forms import ConfirmationForm


class TeamListView(ListView):
    template_name = "teams/team_list.html"
    model = Team

    def get_context_data(self, **kwargs):
        context = super(TeamListView, self).get_context_data(**kwargs)
        context['user_team'] = None
        if self.request.user.team_set.all().exists():
            context['user_team'] = self.request.user.team_set.first()
        return context


class TeamDetailView(DetailView):
    template_name = "teams/team_detail.html"
    model = Team

    def get_context_data(self, **kwargs):
        context = super(TeamDetailView, self).get_context_data(**kwargs)
        context['on_team'] = self.request.user.team_set.filter(pk=self.object.pk).exists()
        return context


class TeamCreateView(CreateView):
    template_name = "teams/team_create.html"
    model = Team
    fields = ['name', 'description']

    def dispatch(self, request, *args, **kwargs):
        if request.user.team_set.all().exists():
            msg = "You must leave your current team before creating another one."
            messages.warning(request, msg)
            return redirect('team_list')
        return super(TeamCreateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        self.request.user.team_set.clear()
        team = form.save()
        team.add_member(self.request.user)
        messages.success(self.request, "Team created!")
        self.request.user.request_set.all().delete()
        return super(TeamCreateView, self).form_valid(form)


class TeamUpdateView(UpdateView):
    template_name = "teams/team_update.html"
    model = Team
    fields = ['name', 'description']

    def dispatch(self, request, *args, **kwargs):
        if not request.user.team_set.all().exists():
            msg = "You must be on a team to update one."
            messages.warning(request, msg)
            return redirect('team_list')
        return super(TeamUpdateView, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user.team_set.first()


class TeamLeaveView(FormView):
    template_name = "teams/team_leave.html"
    form_class = ConfirmationForm

    def dispatch(self, request, *args, **kwargs):
        if not request.user.team_set.all().exists():
            msg = "You must be on a team to leave one."
            messages.warning(request, msg)
            return redirect('team_list')
        return super(TeamLeaveView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("team_list")

    def form_valid(self, form):
        teams = [t.pk for t in self.request.user.team_set.all()]
        self.request.user.team_set.clear()

        for tid in teams:
            team = Team.objects.get(pk=tid)
            if not team.members.exists():
                team.delete()

        msg = "Successfully left team"
        messages.success(self.request, msg)
        return super(TeamLeaveView, self).form_valid(form)


class RequestSendView(FormView):
    template_name = "teams/request_send.html"
    form_class = ConfirmationForm

    def dispatch(self, request, *args, **kwargs):
        self.team = get_object_or_404(Team, slug=kwargs['slug'])
        if self.team.request_set.filter(user=request.user).exists():
            msg = "You already have a pending request for that team"
            messages.info(request, msg)
            return redirect('team_list')
        if request.user.team_set.all().exists():
            msg = "You must leave your current team before requesting to join a new one."
            messages.warning(request, msg)
            return redirect('team_list')

        return super(RequestSendView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(RequestSendView, self).get_context_data(**kwargs)
        context['team'] = self.team
        return context

    def form_valid(self, form):
        team_request = Request.objects.create(team=self.team, user=self.request.user)

        # Send email to team
        for user in self.team.members.all():
            if user.email:
                subject = 'New H4H Team Request!'
                message = render_to_string("teams/request_email.txt",
                                           context={'request': team_request,
                                                    'recipient': user})

                send_mail(subject, message, settings.EMAIL_HOST_USER,
                          [user.email], fail_silently=False)

        messages.success(self.request, "Request sent!")
        return super(RequestSendView, self).form_valid(form)

    def get_success_url(self):
        return reverse("team_list")


class RequestResponseView(FormView):
    template_name = "teams/request_response.html"
    form_class = ConfirmationForm

    def dispatch(self, request, *args, **kwargs):
        self.team_request = get_object_or_404(Request, pk=kwargs['pk'])
        self.team = self.team_request.team
        if not self.team.members.filter(pk=request.user.pk).exists():
            msg = "You cannot respond to that request"
            messages.info(request, msg)
            return redirect('team_list')
        return super(RequestResponseView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(RequestResponseView, self).get_context_data(**kwargs)
        context['team_request'] = self.team_request
        context['team'] = self.team
        return context

    def form_valid(self, form):
        if form.data['action'] == "accept":
            try:
                user = self.team_request.user
                user.team_set.clear()
                user.request_set.all().delete()
                self.team.add_member(user)
                self.team_request.delete()
            except TeamFullException:
                msg = "That team is already full."
                messages.error(self.request, msg)
        elif form.data['action'] == "reject":
            self.team_request.delete()
        return super(RequestResponseView, self).form_valid(form)

    def get_success_url(self):
        return reverse("team_list")


team_list_view = login_required(TeamListView.as_view())
team_detail_view = login_required(TeamDetailView.as_view())
team_create_view = login_required(TeamCreateView.as_view())
team_update_view = login_required(TeamUpdateView.as_view())
team_leave_view = login_required(TeamLeaveView.as_view())

request_send_view = login_required(RequestSendView.as_view())
request_response_view = login_required(RequestResponseView.as_view())
