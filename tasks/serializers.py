from .models import tasks
from rest_framework import serializers


class taskSerializers(serializers.ModelSerializer):
    class Meta:
        model = tasks
        fields = '__all__'
        read_only_fields = ('created_at','modified_at')
