from rest_framework import viewsets
from . import models
from . import serializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializer.Employeserializer