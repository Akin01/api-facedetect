from django.db import models

class tempData(models.Model):
    temp_obj = models.FloatField(null=True)
    temp_env = models.FloatField(null=True)
    img = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

