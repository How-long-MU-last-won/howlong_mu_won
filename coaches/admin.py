from django.contrib import admin
from .models import Coach


# Register your models here.
class trophyWonInline(admin.TabularInline):
    model = Coach.trophyWon.through
    fk_name = "coach"
    extra = 2


class CoachAdmin(admin.ModelAdmin):
    inlines = [trophyWonInline]
    list_display = (
        "name",
        "DOB",
        "numWins",
        "numLosses",
        "numTies",
        "leadFrom",
        "leadTo",
        "statURL",
        "moneySpent",
    )
    list_editable = (
        "numWins",
        "numLosses",
        "numTies",
        "leadFrom",
        "leadTo",
        "statURL",
    )
    search_fields = ("name", "id")
    list_per_page = 25


admin.site.register(Coach, CoachAdmin)
