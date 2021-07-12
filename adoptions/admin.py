from django.contrib import admin
from django.db import models

from .models import Pet


@admin.register(Pet)
class AdminPet(admin.ModelAdmin):
    list_display = ['name', 'description', 'species', 'breed', 'age', 'sex']
