from .models import Song, Singer
from .serializers import SongSerializer, SingerSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class SingerViewset(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class SongViewset(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

