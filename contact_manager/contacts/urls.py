from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactViewSet, websocket_test

router = DefaultRouter()
router.register(r'contacts', ContactViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('ws-test/', websocket_test),
]
