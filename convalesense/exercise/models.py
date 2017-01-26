from __future__ import unicode_literals

from django.db import models

from ..users.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-updated_at', '-created_at',)


class Exercise(BaseModel):
    EXERCISE_TYPES = (
        ('t', 'Duration'),
        ('d', 'Distance'),
    )

    name = models.CharField(max_length=100)
    type_of_exercise = models.CharField(choices=EXERCISE_TYPES, max_length=1)
    type_of_exercise.help_text = 'Particular game type - this determines what is presented back to the users app'
    number_of_reps = models.PositiveSmallIntegerField(default=1)
    number_of_reps.help_text = 'How many times to do this exercise'
    distance = models.FloatField(blank=True, null=True)
    distance.help_text = 'Through distance in cm'
    duration = models.PositiveSmallIntegerField(blank=True, null=True)
    duration.help_text = 'Time in seconds for this exercise'
    score = models.PositiveSmallIntegerField(blank=True, null=True)
    score.help_text = 'Score for this exercise per rep'


class Plan(BaseModel):
    patient = models.ForeignKey(User, related_name='patient')
    therapist = models.ForeignKey(User, related_name='therapist')
    exercises = models.ManyToManyField(Exercise, through='PlanExercise', through_fields=('plan', 'exercise'))
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    description.help_text = 'What this plan aims to achieve for the patient'
    exercises.help_text = 'A plan is composed of multiple exercises which may be in order'
    session_count = models.PositiveSmallIntegerField(default=1, blank=True, null=True)
    session_count.help_text = 'How often the patient should do this plan daily'
    start = models.DateTimeField(blank=True, null=True)
    start.help_text = 'When this treatment plan begins'
    end = models.DateTimeField(blank=True, null=True)
    end.help_text = 'When this treatment plan ends, if at all'


class PlanExercise(BaseModel):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField(blank=True, null=True)
    optional = models.BooleanField(default=False)
    optional.help_text = 'Whether or not this exercise is a required part of the plan'

    class Meta:
        ordering = ('order', 'exercise__name')


class UserSession(BaseModel):
    plan = models.ForeignKey(Plan)


