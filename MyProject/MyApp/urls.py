from django.urls import path
from .views import Index, Challenges, JsonResponseToFrontendIntegration

urlpatterns = [
    path('', Index.as_view()),
    path('JsonResponseToFrontendIntegration', JsonResponseToFrontendIntegration.as_view()),
    path('challenges/<str:month>', Challenges.as_view())
]