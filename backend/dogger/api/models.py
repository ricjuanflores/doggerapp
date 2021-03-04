from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_walker   = models.BooleanField(default=False)
    is_owner    = models.BooleanField(default=False)
    schedule    = models.ManyToManyField('Schedule', blank = True)
    class Meta:
        default_permissions = ('add', 'change', 'delete', 'view')

    def __str__(self):
        return f'{self.first_name} - {self.email} - {self.id}'


class Dog(models.Model):
    DOG_SIZE = (
        (1, 'small'),
        (2, 'medium'),
        (3, 'big')
    )
    name    = models.CharField(max_length=70)
    size    = models.PositiveSmallIntegerField(choices=DOG_SIZE)
    owner   = models.ForeignKey('User', related_name='owner_dog', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.get_size_display()} - Owner: {self.owner}'


class Schedule(models.Model):
     
    small       = models.BooleanField()
    medium      = models.BooleanField()
    big         = models.BooleanField()
    hour_start  = models.TimeField()
    hour_finish = models.TimeField()

    def validate_hours(self):
        if self.hour_start < self.hour_finish:
            return True
        else:
            return False

    def __str__(self):
        _size = ''
        if self.small:
            _size += 'small '
        if self.medium:
            _size += 'medium '
        if self.big:
            _size += 'big'

        return '{} - {} | {}'.format(self.hour_start, self.hour_finish, _size)



class Service(models.Model):

    SERVICE_TYPE = (
        (1, 'reservation'),
        (2, 'offer')
    )

    SERVICE_STATUS = (
        (1, 'confirm'),
        (2, 'reject'),
        (3, 'pending')
    )
    TIME_SERVICE = (
        (1, '30min'),
        (2, '1hr')
    )

    owner           = models.ForeignKey('User', related_name='owner_service', on_delete=models.SET_NULL, null=True, blank=True)
    type            = models.PositiveSmallIntegerField(choices=SERVICE_TYPE)
    date            = models.DateField()
    hour_start      = models.TimeField()
    #hour_finish     = models.TimeField(null=True, blank=True)
    time_service    = models.PositiveSmallIntegerField(choices=TIME_SERVICE)
    #schedule    = models.ForeignKey(Schedule, related_name='schedule_service', on_delete=models.SET_NULL, null=True, blank=True)
    walker          = models.ForeignKey('User', related_name='walker_service', on_delete=models.SET_NULL, null=True, blank=True)
    dogs            = models.ManyToManyField(Dog, blank = True)
    status          = models.PositiveSmallIntegerField(choices=SERVICE_STATUS, default=3)

    def get_quantity_dogs(self):
        return self.dogs.count()

    def hour_finish(self):
        return 'hour finish'

    def __str__(self):
        hour_start = self.hour_start.strftime('%I:%M %p')
        cant = self.get_quantity_dogs()
        return f'{self.get_type_display()} - {self.date} - {hour_start} | {cant} dogs | walker: {self.walker}'