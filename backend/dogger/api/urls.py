from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import MyTokenObtainPairView
from .views import getUserProfile, registerOwner, registerWalker
from .views import createDog, listDogs
from .views import createReservation, createOffer


urlpatterns = [

    # Login
    path('users/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

    # Profile
    path('users/profile/', getUserProfile, name="users-profile"),
    
    # Register
    path('owner/register/', registerOwner, name="owner-register"),
    path('walker/register/', registerWalker, name="walker-register"),

    # Dogs
    path('dog/new/', createDog, name="create-dog"),
    path('dogs/', listDogs, name="list-dog"),

    # Service
    path('service/reservation/', createReservation, name="create-reservation"),
    path('service/offer/', createOffer, name="create-offer"),

]