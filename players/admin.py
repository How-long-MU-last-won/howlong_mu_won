from django.contrib import admin
from .models import Player, Position

# Register your models here.


class PositionAdmin(admin.ModelAdmin):
    list_display = ("id", "position")
    list_editable = ("position",)
    search_fields = ("position",)
    list_per_page = 5


class PlayerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "numGamesPlayed",
        "playFrom",
        "playTo",
        "statURL",
        "boughtBy",
        "position",
        "price",
    )
    list_editable = (
        "name",
        "numGamesPlayed",
        "playFrom",
        "playTo",
        "statURL",
        "boughtBy",
        "position",
        "price",
    )
    search_fields = ("name", "boughtBy", "workWith", "position")
    list_per_page = 25


admin.site.register(Player, PlayerAdmin)
admin.site.register(Position, PositionAdmin)
