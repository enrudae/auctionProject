from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from .models import Lot


class LotSerializer(serializers.ModelSerializer):
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())
    image = Base64ImageField()

    class Meta:
        model = Lot
        exclude = ('is_available',)


class NewBetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lot
        fields = ['id', 'current_price', 'current_buyer']


class BuyersLotsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lot
        fields = '__all__'
