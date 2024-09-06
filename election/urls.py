from django.urls import path
from . import views

urlpatterns = [
    path('candidates/', views.candidate_list, name='candidate_list'),
    path('vote/<int:candidate_id>/', views.vote, name='vote'),
]
