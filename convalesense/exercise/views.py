from django.views.generic import DetailView, ListView
from django.views.generic import TemplateView

from chartit import DataPool, Chart

from .models import Plan, ExerciseRecord, Exercise, PlanExercise


class DashboardView(TemplateView):
    template_name = 'exercise/dashboard.html'

    def get_context_data(self, **kwargs):
        ctx = super(DashboardView, self).get_context_data(**kwargs)
        return ctx


class PlanListView(ListView):
    model = Plan


class ExerciseListView(ListView):
    model = Exercise


class ExerciseDetailView(DetailView):
    model = Exercise


class PlanDetailView(DetailView):
    model = Plan

    def get_context_data(self, **kwargs):
        ctx = super(PlanDetailView, self).get_context_data(**kwargs)

        chart_type = self.request.GET.get('chart_type', 'column')

        exercises = self.get_object().planexercise_set.all()
        if exercises.count() == 0:
            return ctx

        data_series = []
        for plan_exercise in exercises:
            print "    COUNT IS ", ExerciseRecord.objects.filter(exercise=plan_exercise).count()
            data_series.append({
                    'options': {
                        'source': ExerciseRecord.objects.filter(exercise=plan_exercise)
                    },
                    'terms': [
                        {'start_{}'.format(plan_exercise.pk): 'natural_date'},
                        {'{}'.format(plan_exercise.name): 'count'},
                    ]
                })

        data_pool = DataPool(series=data_series)

        chart_terms = {}
        for series in data_series:
            # Super brittle!
            key = series['terms'][0].keys()[0]
            val = series['terms'][1].keys()[0]
            chart_terms.update({ key: [val]})

        chart = Chart(
                datasource = data_pool,
                series_options = [
                    {
                        'options': {
                            'type': chart_type,
                            'stacking': True
                        },
                        'terms': chart_terms,
                    }
                ],
                chart_options = {
                    'title': {'text': 'Patient progress over time'},
                    'xAxis': {'title': {'text': 'Date'}, 'type': 'datetime'},
                }
            )

        ctx.update({'chart': chart})
        return ctx
