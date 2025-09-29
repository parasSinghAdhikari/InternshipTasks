from rest_framework import serializers
from .models import Company,Employees

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  Company
        fields="__all__"

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  Employees
        fields="__all__"
