from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.commands)
class commands(admin.ModelAdmin):
    pass
@admin.register(models.text)
class text(admin.ModelAdmin):
    pass