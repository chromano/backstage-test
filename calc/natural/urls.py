from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import sum_difference

router = DefaultRouter()
app_name = "natural"
urlpatterns = [
    path('difference', sum_difference, name="sum_difference"),

    path('', include(router.urls)),
]
