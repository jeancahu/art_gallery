from django.contrib import admin
from .models import Artwork

class ArtworkAdmin(admin.ModelAdmin):
    list_display = ("name", "collection")
    list_filter = ("name", "collection")
    search_fields = ("name",)

admin.site.register(Artwork, ArtworkAdmin)
