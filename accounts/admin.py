from django.contrib import admin
from .models import BeelineUser


@admin.register(BeelineUser)
class BeelineUserAdmin(admin.ModelAdmin):
    list_display = ('username',)
