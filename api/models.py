from django.db import models

# Create your models here.
class Email(models.Model):
    email_id = models.EmailField()
    email_sub = models.CharField(max_length=50)
    email_body = models.CharField(max_length=1000)