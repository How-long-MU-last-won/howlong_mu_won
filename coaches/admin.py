from django.contrib import admin
from .models import Coach

# Register your models here.


class CoachAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "DOB",
        "numTrophies",
        "numWins",
        "numLosses",
        "numTies",
        "leadFrom",
        "leadTo",
        "moneySpent",
        "statURL",
    )
    list_editable = (
        "name",
        "DOB",
        "numTrophies",
        "numWins",
        "numLosses",
        "numTies",
        "leadFrom",
        "leadTo",
        "moneySpent",
        "statURL",
    )
    search_fields = ("name", "workWith")
    list_per_page = 25


admin.site.register(Coach, CoachAdmin)
