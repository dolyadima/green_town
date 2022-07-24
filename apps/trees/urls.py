from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.trees import views


urlpatterns = [
    path('api/', views.TreesList.as_view()),
    path('api/<int:pk>/', views.TreeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
