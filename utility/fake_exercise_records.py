from datetime import datetime, timedelta
from random import randint, choice
from convalesense.exercise.models import PlanExercise, ExerciseRecord


pes = PlanExercise.objects.all()

for x in range(0, 200):
    start = datetime.now() - timedelta(days=randint(1, 14), minutes=randint(1, 200))
    end = start + timedelta(minutes=randint(1, 10))
    count = randint(3, 17)

    e = ExerciseRecord(start=start, end=end, count=count, exercise=choice(pes))
    e.save()
    print e.pk


