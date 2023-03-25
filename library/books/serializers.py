from rest_framework import serializers
from rest_framework.response import Response
from .models import *

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedBooks
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'