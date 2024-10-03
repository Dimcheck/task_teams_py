from teams.serializers import TeamCreateSerializer, TeamDetailSerializer, AddHumanSerializer, TeamManageSerializer
from teams.models import Team
from rest_framework import generics, views, status, permissions


class TeamAppend(generics.RetrieveUpdateAPIView):
    """
    To extend team, add Human ID to it.
    """

    http_method_names = ('get', 'put')
    serializer_class = AddHumanSerializer
    queryset = Team.objects
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TeamManage(generics.RetrieveUpdateDestroyAPIView):
    """
    Get Team, if you have enough permission - manage it
    To extend team, add Human IDs to it.
    """

    serializer_class = TeamManageSerializer
    queryset = Team.objects
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TeamCreate(generics.CreateAPIView):
    """
    Create Team
    """

    serializer_class = TeamCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class TeamList(generics.ListAPIView):
    """
    Get all Teams
    """

    serializer_class = TeamDetailSerializer
    queryset = Team.objects.all()

