from django.contrib import admin
from .models import Holiday, Leave, Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Holiday)
admin.site.register(Leave)