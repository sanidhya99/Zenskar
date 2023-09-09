from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *
from rest_framework import generics

class CustomerCreateView(generics.ListCreateAPIView):
    serializer_class = customerSerializer

class CustomerEditView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = customerSerializer
    queryset=Customer.objects.all()
    lookup_field='id'     
    


