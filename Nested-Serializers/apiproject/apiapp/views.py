from .models import Song, Singer
from .serializers import SongSerializer, SingerSerializer
from rest_framework import viewsets

# Create your views here.
class SingerViewset(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer

class SongViewset(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
