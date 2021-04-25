from rest_framework import serializers
from .models import Film, Director


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'name']


class FilmFullSerializer(serializers.ModelSerializer):
    director = DirectorSerializer(many=False)

    class Meta:
        model = Film
        fields = ['id', 'title', 'description', 'director',
                  'realase_date', 'movielength']
