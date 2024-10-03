from users.serializers import HumanCreateSerializer, HumanDetailSerializer
from users.models import Human
from django.contrib.auth.hashers import make_password
from rest_framework import generics, permissions, filters


class HumanCreate(generics.CreateAPIView):
    """Create User"""

    serializer_class = HumanCreateSerializer

    def post(self, request, *args, **kwargs):
        data = request.data.copy()

        if data.get('password'):
            data['password'] = make_password(data['password'])
        request._full_data = data
        return super().post(request, *args, **kwargs)


class HumanRetrieve(generics.RetrieveUpdateDestroyAPIView):
    """
    Get User by it's ID and if you have enough permission you can manage it
    """

    serializer_class = HumanDetailSerializer
    queryset = Human.objects
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class HumanList(generics.ListAPIView):
    """Get all Users with their Teams"""

    serializer_class = HumanDetailSerializer
    queryset = Human.objects

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['username', 'email']

