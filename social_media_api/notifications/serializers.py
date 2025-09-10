# notifications/serializers.py
from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.ReadOnlyField(source='actor.username')
    target_repr = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'actor_username', 'verb', 'target_repr', 'created_at', 'read']
        read_only_fields = ['id', 'actor', 'actor_username', 'created_at', 'target_repr']

    def get_target_repr(self, obj):
        
        try:
            return str(obj.target)
        except Exception:
            return None
