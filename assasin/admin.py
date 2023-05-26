from django.contrib import admin
from .models import AssasinProfile, Hit, User


# Register your models here.

admin.site.register(AssasinProfile)
admin.site.register(Hit)
admin.site.register(User)