from dataclasses import field
from django.contrib.auth.models import User, Group
from .models import Book, Student
from rest_framework.serializers import ModelSerializer


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
