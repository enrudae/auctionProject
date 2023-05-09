from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Lot
from .serializers import LotSerializer, NewBetSerializer, BuyersLotsSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly


class ActiveLotsAPIList(generics.ListCreateAPIView):
    queryset = Lot.objects.filter(is_available=True)
    serializer_class = LotSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class LotAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Lot.objects.all()
    serializer_class = LotSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class LotAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Lot.objects.all()
    serializer_class = LotSerializer
    permission_classes = (IsAdminOrReadOnly, )


class NewBetInLotUpdate(generics.RetrieveUpdateAPIView):
    queryset = Lot.objects.filter(is_available=True)
    serializer_class = NewBetSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.creator == request.user:
            return Response({"error: The user cannot perform this action"}, status=403)

        instance.current_price += instance.bet
        instance.current_buyer = request.user
        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class BuyersLotsAPIList(generics.ListCreateAPIView):
    serializer_class = BuyersLotsSerializer

    def get_queryset(self):
        queryset = Lot.objects.filter(current_buyer=self.request.user)
        return queryset


