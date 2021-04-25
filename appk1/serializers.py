from rest_framework import serializers
from .models import Film, Director, Prize, Actor


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['name']

class PrizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prize
        fields = ['name']

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['name']

class FilmFullSerializer(serializers.ModelSerializer):
    director = DirectorSerializer(many=False)
    prize = PrizeSerializer(many=True)
    actors = ActorSerializer(many=True)

    class Meta:
        model = Film
        fields = ['id', 'title', 'description', 'director',
                  'realase_date', 'movielength', 'prize', 'actors']
