from django.http import HttpResponse
from django.shortcuts import render
from .models import Film
from rest_framework import viewsets
from .serializers import FilmFullSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


def first(request):
    films = Film.objects.all()
    return render(request, "first_page.html", {"films": films})

class FilmViewSet(viewsets.ModelViewSet):
    serializer_class = FilmFullSerializer
    queryset = Film.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )