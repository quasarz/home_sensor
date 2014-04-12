from django.shortcuts import render
from rest_framework import viewsets
from api import serializers, models

class SensorNodeViewSet(viewsets.ModelViewSet):
    queryset = models.SensorNode.objects.all()
    serializer_class = serializers.SensorNodeSerializer
