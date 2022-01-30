from django.contrib import admin

# Register your models here.

from app.models import Poll


class PollAdmin(admin.ModelAdmin):

    def save_poll(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        if not change or not instance.created_by:
            instance.created_by = user
        instance.modified_by = user
        instance.save()
        form.save_m2m()
        return instance


admin.site.register(Poll)
