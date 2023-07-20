# views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    # filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    # filterset_fields = [
    #     'owner__following__followed__profile',
    #     'owner__followed__owner__profile',
    # ]
    ordering_fields = [
        'posts_count',
        '-followers_count',
        '-following_count',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


