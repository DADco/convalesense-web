from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets

from .serializers import ExerciseViewSet, PlanViewSet, UserViewSet, PlanExerciseViewSet


router = routers.DefaultRouter()
router.register(r'exercises', ExerciseViewSet)
router.register(r'plans', PlanViewSet)
router.register(r'users', UserViewSet)
router.register(r'plan-exercises', PlanExerciseViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
]
