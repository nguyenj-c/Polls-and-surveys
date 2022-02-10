"""Polls_and_surveys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path

from django.views.i18n import JavaScriptCatalog

from app.views import IndexView, PollsCreateView, PollsListView, LoginFormView, PollsDetailView, PollUpdateView, \
    PollDeleteView, PollVoteView, RegisterFormView, LogoutView, vote, PollsListByUserView, SearchView, SearchRedirectView

urlpatterns = [
]

urlpatterns += i18n_patterns(
    path("jsi18n/", JavaScriptCatalog.as_view(), name="javascript-catalog"),
    path('admin/', admin.site.urls),
    path('index', IndexView.as_view(), name='index'),
    path('polls', PollsListView.as_view(), name='poll_list'),
    path('poll/user', PollsListByUserView.as_view(), name='orderByUser'),
    path('searching', SearchRedirectView.as_view(), name='searching'),
    path('search/<str:search>', SearchView.as_view(), name='searchPoll'),
    path('poll/create', PollsCreateView.as_view(), name='poll_create'),
    path('', LoginFormView.as_view(), name='login'),
    path('register', RegisterFormView.as_view(), name='register'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('polls/<int:pk>', PollsDetailView.as_view(), name='poll_detail'),
    path('poll/update/<int:pk>', PollUpdateView.as_view(), name='poll_update'),
    path('poll/vote/<int:pk>', PollVoteView.as_view(), name='poll_vote'),
    path('poll/vote/submit', vote, name='poll_submit_vote'),
    path('poll/delete/<int:pk>', PollDeleteView.as_view(), name='poll_delete'),
)
