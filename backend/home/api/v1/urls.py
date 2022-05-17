from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import FavoriteCarsViewSet,FavoritesViewSet

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register('favoritecars', FavoriteCarsViewSet )
router.register('favorites', FavoritesViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
