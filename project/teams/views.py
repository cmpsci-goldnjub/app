from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


from .models import Team


class TeamListView(ListView):
    template_name = "teams/team_list.html"
    model = Team


class TeamDetailView(DetailView):
    template_name = "teams/team_detail.html"
    model = Team

    def get_context_data(self, **kwargs):
        context = super(TeamDetailView, self).get_context_data(**kwargs)
        context['teams'] = Team.objects.all()
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
        team = form.save()
        team.members.add(self.request.user)
        messages.success(self.request, "Team created!")
        return super(TeamCreateView, self).form_valid(form)


class TeamUpdateView(UpdateView):
    template_name = "teams/team_update.html"
    model = Team
    fields = ['name', 'description']

    def get_object(self, queryset=None):
        print self.request.user

team_list_view = login_required(TeamListView.as_view())
team_detail_view = login_required(TeamDetailView.as_view())
team_create_view = login_required(TeamCreateView.as_view())
team_update_view = login_required(TeamUpdateView.as_view())
