from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsOwnerUser, IsWalkerUser
# Create your views here.

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserSerializer, UserSerializerWithToken
from .serializers import DogSerializer, ServiceSerializer

from django.contrib.auth.hashers import make_password
from .models import User, Dog, Service, Schedule
from rest_framework import status
from .utils import validate_limite_dogs


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data

        for k, v in serializer.items():
            data[k] = v

        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def getUserProfile(request):
    print("init")
    user = request.user
    print(user)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def registerOwner(request):
    data = request.data
    try:
        user = User.objects.create(
            first_name = data['first_name'],
            username = data['username'],
            email = data['email'],
            password = make_password(data['password']),
            is_owner = True
        )
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail':'El usuario con este email ya existe.'}
        return Response(message, status= status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def registerWalker(request):
    data = request.data
    try:
        user = User.objects.create(
            first_name = data['first_name'],
            username = data['username'],
            email = data['email'],
            password = make_password(data['password']),
            is_walker = True
        )
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail':'El usuario con este email ya existe.'}
        return Response(message, status= status.HTTP_400_BAD_REQUEST)    


@api_view(['POST'])
@permission_classes([IsAuthenticated, IsOwnerUser])
def createDog(request):
    data = request.data
    user = request.user
    print(data)
    try:
        dog = Dog.objects.create(
            name = data['name'],
            size = data['size'],
            owner = user
        )
        print("ra")
        serializer = DogSerializer(dog, many=False)
        return Response(serializer.data)
    except:
        message = {'detail':'Hubo un error inesperado.'}
        return Response(message, status= status.HTTP_400_BAD_REQUEST)   



@api_view(['GET'])
def listDogs(request):
    dogs = Dog.objects.all()
    serializer = DogSerializer(dogs, many=True)
    return Response(serializer.data)




@api_view(['POST'])
@permission_classes([IsAuthenticated, IsOwnerUser])
def createReservation(request):
    data = request.data
    user = request.user
    type_service = 1
    dogs = Dog.objects.filter(id__in=data['dogs'])
    hour_start  = data['hour_start']
    hour_finish = data['hour_finish']
    #status = data["status"]

    if validate_limite_dogs(user, data, type_service):
        if data['walker']:
            walker_id = data['walker']
            walker = User.objects.get(id=walker_id)
            service = Service.objects.create(
                type = type_service, #reservation 
                hour_start = hour_start,
                hour_finish = hour_finish,
                walker = walker,
                owner = user
            )
            service.dogs.add(*dogs)

            serializer = ServiceSerializer(service, many=False)
            return Response(serializer.data)
    else:
        message = {'detail':'Solo puedes asignar hasta 3 perros por hora'}
        return Response(message, status= status.HTTP_400_BAD_REQUEST)   


@api_view(['POST'])
@permission_classes([IsAuthenticated, IsOwnerUser])
def createOffer(request):
    data = request.data
    user = request.user

    dogs = Dog.objects.filter(id__in=data['dogs'])
    hour_start  = data['hour_start']
    hour_finish = data['hour_finish']
    #status = data["status"]
        
    service = Service.objects.create(
        type = 2, #offer
        hour_start = hour_start,
        hour_finish = hour_finish,
        owner = user
    )
    service.dogs.add(*dogs)
    serializer = ServiceSerializer(service, many=False)
    return Response(serializer.data)    