
from .models import Service

def validate_limite_dogs(user, data, type_service):
    hour_start = data["hour_start"]
    #9am - 10am
    #9am - 10am
    #9am - 10am
    #5pm - 6pm

    #9am - 10am

    #Cantidad de servicios confirmados en la misma hora.
    servicios = Service.objects.filter(owner=user, hour_start=hour_start, status=1, type=type_service)

    #Cantidad de perros asignados en estos servicios.
    perros = servicios.annotate(num_dogs = Count('dogs'))

    if servicios == 3:
        return False
    else:
        return True
    