from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets

from .serializers import ExerciseViewSet


router = routers.DefaultRouter()
router.register(r'exercises', ExerciseViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
]
