from rest_framework import serializers, permissions
from .models import Event, Technical, Changes, Deleted_Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'created', 'title', 'address', 'owner', 'technical', 'description', 'date', 'start_time', 'end_time']

class ChangesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Changes
        fields = '__all__'

class TechnicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technical
        fields = '__all__'

class DeletedEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deleted_Event
        fields = '__all__'