from django.contrib import admin
from .models import Complain, Bug
# Register your models here.

admin.site.register(Complain)
admin.site.register(Bug)