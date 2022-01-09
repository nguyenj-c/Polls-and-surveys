from django.contrib import admin

# Register your models here.

from app.models import Poll


admin.site.register(Poll)
