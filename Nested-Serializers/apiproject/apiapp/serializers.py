from dataclasses import fields
from rest_framework import serializers
from .models import Song, Singer


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'singer', 'year']

class SingerSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True, read_only=True)
    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'songs']