from rest_framework import serializers

from .models import tempData

class tempSerializer(serializers.ModelSerializer):
    class Meta:
        model = tempData
        fields = '__all__'
