from django.contrib.auth.decorators import login_required
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


class TeamCreateView(CreateView):
    template_name = "teams/team_create.html"
    model = Team
    fields = ['name', 'description']


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
