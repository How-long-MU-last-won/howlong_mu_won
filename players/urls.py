from django.urls import path
from . import views

urlpatterns = [
    path("", views.getPlayers, name="players"),
    path("<int:pk>/", views.getPlayer, name="player"),
    path(
        "bought/<int:coach_id>/",
        views.getByCoachBought,
        name="playerByCoachBought",
    ),
    path(
        "workwith/<int:pk>/",
        views.getAllCoachesWorkWith,
        name="playerByCoachWorkWith",
    ),
    path("pos/<int:position_id>/", views.getByPosition, name="playerByPosition"),
]
