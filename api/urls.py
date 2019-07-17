from rest_framework import routers

from django.urls import path, include

from .views import EventViewSet

app_name = 'api'

router = routers.DefaultRouter()

router.register(r'event', EventViewSet)

urlpatterns = [
    path('', include(router.urls))
]
