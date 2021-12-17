from django.contrib import admin

from .models import tempData

class tempField(admin.ModelAdmin):
    list_display = ['temp_obj', 'temp_env', 'img', 'created_at']

admin.site.register(tempData, tempField)
