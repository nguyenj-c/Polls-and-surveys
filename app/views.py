from django.http import HttpResponseForbidden
from django.shortcuts import render

from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, FormView, DeleteView

from app.forms.login import LoginForm
from app.models import Poll


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['title'] = 'Home'
        return result


class PollsCreateView(CreateView):
    template_name = "poll_create.html"
    model = Poll
    fields = ('Question', 'option_1', 'option_2', 'option_3', 'option_4')
    success_url = reverse_lazy('poll_list')

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['title'] = 'Create poll'
        return result


class PollsListView(ListView):
    template_name = "poll_list.html"
    model = Poll

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['title'] = 'List of poll'
        return result


class PollsDetailView(LoginRequiredMixin, DetailView):
    template_name = "poll_detail.html"
    model = Poll
    fields = ('Question', 'option_1', 'option_2', 'option_3', 'option_4')

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['title'] = 'Detail poll'
        return result


class PollUpdateView(UpdateView):
    template_name = "poll_create.html"
    model = Poll
    fields = ('Question', 'option_1', 'option_2', 'option_3', 'option_4')
    success_url = reverse_lazy('poll_list')

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['title'] = 'Update poll'
        return result


class PollDeleteView(DeleteView):
    template_name = "poll_list.html"
    model = Poll
    http_method_names = ['delete']
    success_url = reverse_lazy('poll_list')

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['title'] = 'Delete poll'
        return result

    def dispatch(self, request, *args, **kwargs):
        # safety checks go here ex: is user allowed to delete?
        if request.user.username != kwargs['username']:
            return HttpResponseForbidden()
        else:
            handler = getattr(self, 'delete')
            return handler(request, *args, **kwargs)


class LoginFormView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = "/poll/create"

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            messages.add_message(
                self.request, messages.INFO,
                f'Hello {user.username}!'
            )
            return super().form_valid(form)

        return super().form_invalid(form)

