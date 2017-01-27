from rest_framework import routers, serializers, viewsets
from .models import Exercise, Plan, PlanExercise, ExerciseRecord
from ..users.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:user-detail')
    type = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'name', 'type')

    def get_type(self, obj):
        return obj.get_type_display().lower()

    def get_name(self, obj):
        return obj.get_full_name()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ExerciseSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:exercise-detail')
    type_of_exercise = serializers.SerializerMethodField()

    class Meta:
        model = Exercise
        fields = ('id', 'url', 'name', 'description', 'type_of_exercise',
                  'number_of_reps', 'duration', 'distance', 'score')

    def get_type_of_exercise(self, obj):
        return obj.get_type_of_exercise_display().lower()


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class PlanExerciseSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:planexercise-detail')
    name = serializers.ReadOnlyField(source='exercise.name')
    score = serializers.ReadOnlyField(source='exercise.score')
    type = serializers.SerializerMethodField()
    weight = serializers.SerializerMethodField()
    duration = serializers.SerializerMethodField()
    distance = serializers.SerializerMethodField()
    repetitions = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = PlanExercise
        fields = ('id', 'url', 'order', 'count', 'name', 'type', 'score',
                  'distance', 'repetitions', 'weight', 'duration', 'description')

    def get_type(self, obj):
        return obj.exercise.get_type_of_exercise_display().lower()

    def get_weight(self, obj):
        if obj.weight:
            return obj.weight
        return obj.exercise.weight

    def get_duration(self, obj):
        if obj.duration:
            return obj.duration
        return obj.exercise.duration

    def get_distance(self, obj):
        if obj.distance:
            return obj.distance
        return obj.exercise.distance

    def get_repetitions(self, obj):
        if obj.number_of_reps:
            return obj.number_of_reps
        return obj.exercise.number_of_reps

    def get_description(self, obj):
        if obj.additional_description:
            return '{}\n{}'.format(obj.exercise.description, obj.additional_description)
        return obj.exercise.description


class PlanExerciseViewSet(viewsets.ModelViewSet):
    queryset = PlanExercise.objects.all()
    serializer_class = PlanExerciseSerializer


class PlanSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:plan-detail')
    therapist = UserSerializer(read_only=True)
    patient = UserSerializer(read_only=True)
    exercises = PlanExerciseSerializer(many=True, source='planexercise_set', read_only=True)

    class Meta:
        model = Plan
        fields = ('id', 'url', 'name', 'description', 'start', 'end',
                  'therapist', 'patient', 'exercises')


class PlanViewSet(viewsets.ModelViewSet):
    serializer_class = PlanSerializer

    def get_queryset(self):
        is_android = self.request.GET.get('android', None) is not None
        is_ios = self.request.GET.get('ios', None) is not None

        if is_android:
            qs = Plan.objects.filter(tag='a')
        elif is_ios:
            qs = Plan.objects.filter(tag='i')
        else:
            qs= Plan.objects.all()

        return qs


class ExerciseRecordSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:exerciserecord-detail')
    exercise_id = serializers.PrimaryKeyRelatedField(source='exercise', queryset=PlanExercise.objects.all())

    class Meta:
        model = ExerciseRecord
        fields = ('url', 'created_at', 'id', 'count', 'start', 'end', 'exercise_id')

    def create(self, validated_data):
        record = ExerciseRecord.objects.create(
            exercise=validated_data['exercise'],
            start=validated_data['start'],
            end=validated_data['end'],
            count=validated_data['count']
        )

        return record


class ExerciseRecordViewSet(viewsets.ModelViewSet):
    queryset = ExerciseRecord.objects.all()
    serializer_class = ExerciseRecordSerializer

    # def create(self, request):
    #     import ipdb; ipdb.set_trace()
    #     return super(ExerciseRecordViewSet, self).create(request)
