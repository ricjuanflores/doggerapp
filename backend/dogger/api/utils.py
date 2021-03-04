
from .models import Service
from django.db.models import Count, Sum

def validate_limite_dogs(user, data, type_service):
    hour_start = data["hour_start"]
    date = data["date"]

    #Cantidad de servicios confirmados en la misma hora.
    servicios = Service.objects.filter(owner=user, date = date, hour_start=hour_start, status=1, type=type_service)
    print(servicios)

    #Cantidad de perros asignados a cada servicio.
    perros = servicios.annotate(num_dogs = Count('dogs'))

    #Numero total de perros de estos servicios.
    num_dogs = perros.aggregate(sum_dogs=Sum('num_dogs'))['sum_dogs'] or False

    print('num_dogs')
    print(num_dogs)

    if num_dogs >= 3:
        return False
    else:
        return True
    