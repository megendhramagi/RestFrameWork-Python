from rest_framework.serializers import ModelSerializer
from .models import Book

class BookSerial(ModelSerializer):
    class Meta:
        model = Book
        fields="__all__"