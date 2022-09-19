from auth_shop.forms import RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic


def index(request):
    """View function for shop home page"""
    return render(request, 'index.html')


class RegisterFormView(SuccessMessageMixin, generic.FormView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_message = "Profile has been registered"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        user = form.save()
        password = form.cleaned_data.get("password1")
        user = authenticate(username=user.username, password=password)
        login(self.request, user)
        return super(RegisterFormView, self).form_valid(form)


class UpdateProfile(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = User
    fields = ["username", "email"]
    template_name = 'registration/update_profile.html'
    success_url = reverse_lazy("index")
    success_message = "Profile updated"

    def get_object(self, queryset=None):
        user = self.request.user
        return user


class UserProfile(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = "registration/profile.html"

    def get_object(self, queryset=None):
        user = self.request.user
        return user

    def get_context_data(self, **kwargs):
        context = super(UserProfile, self).get_context_data(**kwargs)
        return context
