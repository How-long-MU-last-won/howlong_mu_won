from django.urls import path
from . import views

urlpatterns = [
    path("", views.getCoaches, name="coaches"),
    path("<int:pk>/", views.getCoach, name="coach"),
    path(
        "workwith/<int:pk>/",
        views.getAllPlayersWorkWith,
        name="playerByCoachWorkWith",
    ),
]
