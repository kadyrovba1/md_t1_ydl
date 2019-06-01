from django.contrib import admin
from .models import Download
# Register your models here.
class RatingAdmin(admin.ModelAdmin):
    list_display = ('upload', 'download_date')
admin.site.register(Download)