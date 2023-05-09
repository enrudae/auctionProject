from django.db import models
from django.contrib.auth.models import User


class Lot(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='lot_pics', null=True, blank=True)

    #first_price = models.DecimalField(max_digits=10, decimal_places=2) # расписать все эти ограничения дине
    #current_price = models.DecimalField(max_digits=10, decimal_places=2)
    first_price = models.IntegerField() # расписать все эти ограничения дине
    current_price = models.IntegerField()
    bet = models.IntegerField()
    creation_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField()
    is_available = models.BooleanField(default=True)
    creator = models.ForeignKey(User, verbose_name='Создатель', related_name='Creator', on_delete=models.CASCADE)
    current_buyer = models.ForeignKey(User, verbose_name='Покупатель', related_name='Buyer', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
