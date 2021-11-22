from django.shortcuts import render
from rest_framework import generics, status
from .serializers import ItemSerializer
from .models import Item, Category
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class ItemView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer