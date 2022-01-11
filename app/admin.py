from django.contrib import admin

# Register your models here.

from app.models import Question


class QuestionAdmin(admin.TabularInline):
    model = Question
    extra = 0
