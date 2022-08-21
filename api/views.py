from django.shortcuts import render
from .models import Email
from .serializer import EmailSerializer
from rest_framework import viewsets
# Create your views here.


class EmailModelViewSet(viewsets.ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer