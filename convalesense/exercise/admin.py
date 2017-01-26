from django.contrib import admin

# Register your models here.
from .models import Exercise, Plan, UserSession


class BaseAdmin(admin.ModelAdmin):
    pass


class ExerciseAdmin(BaseAdmin):
    pass


class PlanAdmin(BaseAdmin):
    pass


class UserSessionAdmin(BaseAdmin):
    pass


admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(UserSession, UserSessionAdmin)
