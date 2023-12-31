from django.contrib import admin
from .models import Trophy

# Register your models here.


class TrophyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "lastWonDate", "numTimesWon")
    search_fields = ("id", "name")
    list_per_page = 25


admin.site.register(Trophy, TrophyAdmin)
