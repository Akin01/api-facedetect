from django.db import models

class tempData(models.Model):
    temp = models.FloatField()
    img = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

