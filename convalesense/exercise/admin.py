from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
from .models import Exercise, Plan, UserSession, PlanExercise


class BaseAdmin(SummernoteModelAdmin):
    list_display = ('id', 'created_at')


class PlanExerciseInline(admin.StackedInline):
    model = PlanExercise


class ExerciseAdmin(BaseAdmin):
    list_display = BaseAdmin.list_display + ('name', 'type_of_exercise')
    list_filter = ('type_of_exercise', )
    list_display_links = ('id', 'name')
    fieldsets = (
        (None, {
            'fields': ('name', 'type_of_exercise', 'description')
        }),
        ('Common', {
            'fields': ('number_of_reps', 'weight', 'score',),
        }),
        ('Duration games', {
            'fields': ('duration',),
        }),
        ('Distance games', {
            'fields': ('distance',),
        }),
    )

class PlanAdmin(BaseAdmin):
    list_display = BaseAdmin.list_display + ('name', 'patient', 'therapist', 'exercise_count')
    list_display_links = ('id', 'name')
    list_filter = ('patient', 'therapist')
    inlines = [PlanExerciseInline, ]


class UserSessionAdmin(BaseAdmin):
    pass


admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(UserSession, UserSessionAdmin)
