from django.views.generic import DetailView
from chartit import DataPool, Chart

from .models import Plan, ExerciseRecord


class PlanDetailView(DetailView):
    model = Plan

    def get_context_data(self, **kwargs):
        ctx = super(PlanDetailView, self).get_context_data(**kwargs)

        exercise_records = \
            DataPool(
               series=
                [{'options': {
                   'source': ExerciseRecord.objects.all()},
                  'terms': [
                    'start',
                    'count']}
                 ])

        chart = Chart(
                datasource = exercise_records,
                series_options =
                  [{'options':{
                      'type': 'line',
                      'stacking': False},
                    'terms':{
                      'start': [
                        'count']
                      }}],
                chart_options =
                  {'title': {
                       'text': 'Patient progress over time'},
                   'xAxis': {
                        'title': {
                           'text': 'Date'}}})

        ctx.update({'chart': chart})
        return ctx

