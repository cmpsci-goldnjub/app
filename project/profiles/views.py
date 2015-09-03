from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Profile


class ProfileListView(ListView):
    template_name = "profiles/profile_list.html"
    model = Profile


class ProfileDetailView(DetailView):
    template_name = "profiles/profile_detail.html"
    model = Profile


class ProfileUpdateView(UpdateView):
    template_name = "profiles/profile_update.html"
    model = Profile
    fields = ['name', 'about_me']


profile_list_view = login_required(ProfileListView.as_view())
profile_detail_view = login_required(ProfileDetailView.as_view())
profile_update_view = login_required(ProfileUpdateView.as_view())
