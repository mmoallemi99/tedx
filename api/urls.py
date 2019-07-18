from rest_framework import routers

from django.urls import path, include

from .views import EventViewSet, StaffViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'event', EventViewSet)
router.register(r'staff', StaffViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('', EventViewSet.as_view, name='event'),
]
