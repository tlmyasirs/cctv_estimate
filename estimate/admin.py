from django.contrib import admin

# Register your models here.
from .models import Cam

@admin.register(Cam)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'mp','price']