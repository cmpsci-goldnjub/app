from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Profile
from .forms import ProfileForm


class ProfileListView(ListView):
    template_name = "profiles/profile_list.html"
    model = Profile


class ProfileDetailView(DetailView):
    template_name = "profiles/profile_detail.html"
    model = Profile

    def get_object(self, queryset=None):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])


class ProfileUpdateView(FormView):
    template_name = "profiles/profile_update.html"
    form_class = ProfileForm

    def get_initial(self):
        user = self.request.user
        return {'first_name': user.first_name,
                'last_name': user.last_name,
                'status': user.profile.status,
                'about_me': user.profile.about_me}

    def get_context_data(self, **kwargs):
        context = super(ProfileUpdateView, self).get_context_data(**kwargs)
        context['profile'] = self.request.user.profile
        return context

    def form_valid(self, form):
        user = self.request.user
        user.first_name = form.cleaned_data["first_name"]
        user.last_name = form.cleaned_data["first_name"]
        user.profile.status = form.cleaned_data["status"]
        user.profile.about_me = form.cleaned_data["about_me"]
        user.profile.save()
        user.save()
        return super(ProfileUpdateView, self).form_valid(form)

    def get_success_url(self):
        return self.request.user.profile.get_absolute_url()


profile_list_view = login_required(ProfileListView.as_view())
profile_detail_view = login_required(ProfileDetailView.as_view())
profile_update_view = login_required(ProfileUpdateView.as_view())
