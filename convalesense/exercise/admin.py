from django.contrib import admin

# Register your models here.
from .models import Exercise, Plan, UserSession


class BaseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'created_at')


class ExerciseAdmin(BaseAdmin):
    list_display = BaseAdmin.list_display + ('name', 'type_of_exercise')
    list_filter = ('type_of_exercise', )
    fieldsets = (
        (None, {
            'fields': ('name', 'type_of_exercise')
        }),
        ('Common', {
            'fields': ('number_of_reps', 'score',),
        }),
        ('Duration games', {
            'fields': ('duration',),
        }),
        ('Distance games', {
            'fields': ('distance',),
        }),
    )

class PlanAdmin(BaseAdmin):
    pass


class UserSessionAdmin(BaseAdmin):
    pass


admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(UserSession, UserSessionAdmin)
