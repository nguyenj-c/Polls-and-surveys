from django.shortcuts import render
from msilib.schema import ListView
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, FormView

from app.forms.login import LoginForm
from app.models import Question


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['title'] = 'Page principale'
        return result


class QuestionCreateView(CreateView):
    template_name = "question_create.html"
    model = Question
    fields = ('Sujet', 'Question')
    success_url = reverse_lazy('question_list')


class QuestionListView(ListView):
    template_name = "question_list.html"
    model = Question


class LoginFormView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = "/"

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
        #form.add_error(None, "email / mdp invalid")
        return super().form_invalid(form)

