from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import BookSerial 
from .models import Book
# Create your views here.

class BookView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerial
