from .models import Employee
#import serializer  
from rest_framework import serializers


class Employeserializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
