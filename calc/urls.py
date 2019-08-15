from django.urls import path, include


urlpatterns = [
    path('api/v1/calc/', include('calc.natural.urls', namespace="calc")),
]
