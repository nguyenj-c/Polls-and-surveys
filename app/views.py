from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, FormView, DeleteView, RedirectView
from app.forms.login import LoginForm, RegisterForm
from app.models import Poll


class IndexView(ListView):
    template_name = "index.html"
    model = Poll

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['title'] = 'Home'
        return result


class PollsCreateView(LoginRequiredMixin, CreateView):
    template_name = "poll_create.html"
    model = Poll
    exclude = ['author']
    fields = ('Question', 'option_1', 'option_2', 'option_3', 'option_4')
    success_url = reverse_lazy('poll_list')

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['title'] = 'Create poll'
        return result

    def form_valid(self, form):
        poll = form.save(commit=False)
        poll.author = self.request.user
        poll.save()
        return super().form_valid(form)


def current_user(self):
    return self.request.user


class PollsListView(LoginRequiredMixin, ListView):
    template_name = "poll_list.html"
    model = Poll

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['title'] = 'List of poll'
        result["polls"] = Poll.objects.filter(
            author__username=current_user(self)
        )
        return result


class PollsListByUserView(ListView):
    template_name = "poll_orderBy_user.html"
    model = Poll

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['title'] = 'List of poll'
        result["authors"] = User.objects.all()
        result["pollsByAuthor"] = Poll.objects.all().order_by("author__username")
        return result


class SearchView(ListView):
    template_name = "poll_search.html"
    model = Poll

    def get_context_data(self, *, object_list=None, **kwargs):
        result = super(SearchView, self).get_context_data(**kwargs)
        result['title'] = 'Search of poll'
        result["searchPoll"] = Poll.objects.filter(author__username=self.kwargs["search"]).all()
        result["searchResult"] = self.kwargs["search"]
        return result


class SearchRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        search = self.request.POST["poll-search"]
        if search == "":
            return reverse_lazy("polls")
        else:
            return reverse_lazy("searchPoll", kwargs={"search": search})


class PollsDetailView(DetailView):
    template_name = "poll_detail.html"
    model = Poll
    fields = ('Question', 'option_1', 'option_2', 'option_3', 'option_4')

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['title'] = 'Detail poll'
        return result


class PollUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "poll_create.html"
    model = Poll
    fields = ('Question', 'option_1', 'option_2', 'option_3', 'option_4')
    success_url = reverse_lazy('poll_list')

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['title'] = 'Update poll'
        return result


class PollDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "poll_delete.html"
    model = Poll
    success_url = "/index"


class PollVoteView(DetailView):
    template_name = "poll_vote.html"
    model = Poll
    success_url = "/index"

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['title'] = 'Vote'
        return result


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
        confirm_password = form.cleaned_data["confirm_password"]

        if password != confirm_password:
            form.add_error('confirm_password', "Password does not match")
            return super().form_invalid(form)

        duplicate_users = User.objects.filter(username=username)
        if duplicate_users.exists():
            form.add_error('username', "This username is already registered!")
            return super().form_invalid(form)
        user = User.objects.create_user(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        return super().form_invalid(form)


class LogoutView(SuccessMessageMixin, TemplateView):
    def get(self, request, **kwargs):
        logout(request)
        return redirect("/")
