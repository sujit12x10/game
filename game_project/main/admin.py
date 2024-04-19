from django.contrib import admin
from main.models import Season, Match, Team, PointsTable

# Register your models here.
class MatchesInline(admin.TabularInline):
    model = Match

class SeasonAdmin(admin.ModelAdmin):
    inlines = [MatchesInline]

admin.site.register(Season, SeasonAdmin)
admin.site.register(Match)
admin.site.register(Team)
admin.site.register(PointsTable)
