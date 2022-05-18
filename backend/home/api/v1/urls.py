from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import FavoriteCarsViewSet,FavoritesViewSet,TomTestViewSet

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register('favoritecars', FavoriteCarsViewSet )
router.register('favorites', FavoritesViewSet )
router.register('tomtest', TomTestViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
