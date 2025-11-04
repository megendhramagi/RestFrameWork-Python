from rest_framework.serializers import ModelSerializer
from .models import Students, Marks

class StudentSerial(ModelSerializer):
    class Meta():
        model = Students
        fields = "__all__"

class MarkSerial(ModelSerializer):
    class Meta():
        model = Marks
        fields = "__all__"