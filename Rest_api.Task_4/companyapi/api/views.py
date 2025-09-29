from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework.decorators import action 
from .models import Company,Employees
from .serilizers import CompanySerializer,EmployeeSerializer
from rest_framework.response import Response

# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        company = Company.objects.get(pk=pk)
        emps = Employees.objects.filter(company_Id=company)
        emps_serializer = EmployeeSerializer(emps,many=True,context ={'request':request})
        return Response(emps_serializer.data)

    


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer    