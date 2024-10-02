from rest_framework import serializers
from teams.models import Team


class TeamCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name']


class TeamDetailSerializer(serializers.ModelSerializer):
    # human = serializers.ReadOnlyField(source='human.username')
    members = serializers.StringRelatedField(many=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'members']


class AddHumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name', 'members']


