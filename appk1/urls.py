from django.urls import path, include
from . import views
from rest_framework import routers
from .views import FilmViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register('film', FilmViewSet)
urlpatterns = [
    path('hello/', views.first, name='first'),
    path('', include(router.urls)),
    path('auth/', obtain_auth_token),
]
