from rest_framework import serializers
from teams.models import Team

from users.models import Human


class HumanCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Human
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


class HumanDetailSerializer(serializers.ModelSerializer):
    team = serializers.PrimaryKeyRelatedField(
        queryset=Team.objects.all(),
        many=True,
    )

    class Meta:
        model = Human
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'team']

