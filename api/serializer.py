from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Email

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email 
        fields = ['id','email_id','email_sub','email_body']

    # def validate(self, attrs):
    #     attrs['email_id'] = attrs['email_id'].replace(',',' ')
    #     return super().validate(attrs)