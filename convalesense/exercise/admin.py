from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
from .models import Exercise, Plan, PlanExercise, ExerciseRecord


class BaseAdmin(SummernoteModelAdmin):
    list_display = ('id', 'created_at', 'tag')


class PlanExerciseAdmin(BaseAdmin):
    list_display = ('id', 'exercise', 'created_at', 'plan')
    list_filter = ('plan', 'exercise')


class PlanExerciseInline(admin.StackedInline):
    model = PlanExercise
    fieldsets = (
        (None, {
            'fields': ('exercise', 'order', 'count')
        }),
        ('Extra information for the patient', {
            'fields': ('additional_description', 'image')
        }),
        ('Customization of this exercise', {
            'fields': ('number_of_reps', 'distance',  'duration', 'score', 'weight'),
        }),
    )


class ExerciseAdmin(BaseAdmin):
    list_display = BaseAdmin.list_display + ('name', 'type_of_exercise')
    list_filter = ('type_of_exercise', )
    list_display_links = ('id', 'name')
    fieldsets = (
        (None, {
            'fields': ('name', 'type_of_exercise', 'image', 'tag')
        }),
        ('Guidance', {
            'fields': ('description', 'steps'),
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


class ExerciseRecordAdmin(BaseAdmin):
    list_display = ('id', 'created_at', 'exercise')


admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(PlanExercise, PlanExerciseAdmin)
admin.site.register(ExerciseRecord, ExerciseRecordAdmin)
