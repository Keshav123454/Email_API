from django.contrib import admin
from .models import Email

# Register your models here.
@admin.register(Email)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','email_id','email_sub','email_body']