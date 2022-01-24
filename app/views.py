from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, FormView, DeleteView

from app.forms.login import LoginForm, RegisterForm
from app.models import Poll


class IndexView(ListView):
    template_name = "index.html"
    model = Poll

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


class PollsListView(LoginRequiredMixin, ListView):
    template_name = "poll_list.html"
    model = Poll

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['title'] = 'List of poll'
        return result


class PollsDetailView(DetailView):
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
    template_name = "poll_delete.html"
    model = Poll
    success_url = "/index"


class PollVoteView(DeleteView):
    template_name = "poll_vote.html"
    model = Poll
    success_url = "/index"

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['title'] = 'Vote'
        return result


class PollSubmitVoteView(View):
    template_name = "poll_vote.html"
    model = Poll


def vote(request):
    poll = Poll.objects.get(pk=request.POST['id'])

    if request.method == 'POST':
        selected_option = request.POST['poll']
    if selected_option == 'option1':
        poll.option_1_count += 1
    elif selected_option == 'option2':
        poll.option_2_count += 1
    elif selected_option == 'option3':
        poll.option_3_count += 1
    elif selected_option == 'option4':
        poll.option_4_count += 1
    else:
        return "Not valid"
    poll.save()
    return redirect('/index')


class LoginFormView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = "index"

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            messages.add_message(
                self.request, messages.INFO,
                f'Hello {user.username} you can choose a poll and vote!'
            )
            return super().form_valid(form)

        return super().form_invalid(form)


class RegisterFormView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    form = UserCreationForm()
    success_url = "index"

    def form_valid(self, form):
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, password=password)
            if user is not None:
                login(self.request, user)
                return super().form_valid(form)
            return super().form_invalid(form)


def logout_view(request):
    logout(request)
    return redirect('/')
