from django.shortcuts import render
from rest_framework import generics

from cars.serializers import CarDetailSerializer, CarListSerializer

from cars.models import Car

from cars.permisions import IsOwnerOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer


class CarsListView(generics.ListAPIView):
    serializer_class = CarListSerializer
    queryset = Car.objects.all()
    permission_classes = (IsAdminUser,)


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (IsOwnerOrReadOnly,)
