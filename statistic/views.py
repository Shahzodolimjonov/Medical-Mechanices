from django.db.models import Count, Sum
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class EmployeeAPIView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class ClientAPIView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = PtoductSerializer


class OrderAPIView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class EmployeeStatistics(generics.RetrieveAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        month = self.request.query_params.get('month')
        year = self.request.query_params.get('year')
        return Employee.objects.annotate(
            total_clients=Count('order__client', distinct=True),
            total_products=Count('order__products'),
            tolal_sales=Sum('order__price')
        ).filter(order__date__month=month, order__date__year=year)


class AllEmployeesStatistics(generics.ListAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        month = self.request.query_params.get('month')
        year = self.request.query_params.get('year')
        return Employee.objects.annotate(
            total_clients=Count('order__client', distinct=True),
            total_products=Count('order__products'),
            total_sales=Sum('order__price')
        ).filter(order__date__month=month, order__date__year=year)


class ClientStatistics(generics.RetrieveAPIView):
    serializer_class = ClientSerializer

    def get_queryset(self):
        month = self.request.query_params.get('month')
        year = self.request.query_params.get('year')
        return Client.objects.annotate(
            total_products=Count('order__products'),
            total_sales=Sum('order__price')
        ).filter(order__date__month=month, order__date__year=year)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["employee"]


