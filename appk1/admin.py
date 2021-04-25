from django.contrib import admin
from .models import Film, Director, Prize, Actor
# Register your models here.

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ['title', 'realase_date']
    list_filter = ['movielength']
    search_fields = ['title', 'description']

admin.site.register(Director)
admin.site.register(Prize)
admin.site.register(Actor)