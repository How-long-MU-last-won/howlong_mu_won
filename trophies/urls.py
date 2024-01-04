from django.urls import path
from . import views

urlpatterns = [
    path("", views.getTrophies, name="trophies"),
    path("<int:pk>/", views.getTrophy, name="trophy"),
    path("coach/<int:coach_id>/", views.getTrophyByCoach, name="trophyByCoach"),
]
