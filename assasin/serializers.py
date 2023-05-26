from rest_framework import serializers
from .models import AssasinProfile, Hit

class AssasinSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssasinProfile
        fields = "__all__"
        
        
class HitSerializer(serializers.ModelSerializer):
    hitman = serializers.CharField(source='hitman.user.username', read_only=True)

    class Meta:
        model = Hit
        fields = ['id', 'hitman', 'price', 'target']