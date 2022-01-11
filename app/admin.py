from django.contrib import admin

# Register your models here.

from app.models import Polls


class QuestionAdmin(admin.TabularInline):
    model = Polls
    extra = 0


admin.site.register(Polls)