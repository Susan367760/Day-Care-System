from django.contrib import admin
from .models import Parent, Child, CheckIn

admin.site.register(Parent)
admin.site.register(Child)
admin.site.register(CheckIn)
