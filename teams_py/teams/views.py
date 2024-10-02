from teams.serializers import TeamCreateSerializer, TeamDetailSerializer, AddHumanSerializer
from teams.models import Team
from rest_framework import generics, permissions

from rest_framework import generics, permissions


class TeamAppend(generics.RetrieveUpdateDestroyAPIView):
    """
    Get Team, if you have enough permission - manage it
    To extend team, add Human IDs to it.
    """

    serializer_class = AddHumanSerializer
    queryset = Team.objects.all()
    permission_classes = [
        # permissions.IsAuthenticatedOrReadOnly,
        # custom_permissions.IsOwnerOrReadOnly,
    ]


class TeamCreate(generics.CreateAPIView):
    """
    Create Team
    """

    serializer_class = TeamCreateSerializer
    # permission_classes = [permissions.IsAuthenticated]



class TeamList(generics.ListAPIView):
    """
    Get all Teams
    """

    serializer_class = TeamDetailSerializer
    queryset = Team.objects.all()

