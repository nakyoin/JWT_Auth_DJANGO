from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from django.forms.models import model_to_dict
from .serializers import *
from rest_framework.generics import *

class BookApiView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookApiCrud(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_class = (TokenAuthentication, )
    permission_classes = (IsAdminUser, )

class OrderedApiView(ListAPIView):
    queryset = OrderedBooks.objects.all()
    serializer_class = OrderSerializer
    authentication_class = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)

class OrderedApiCrud(RetrieveUpdateDestroyAPIView):
    queryset = OrderedBooks.objects.all()
    serializer_class = OrderSerializer
    authentication_class = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)