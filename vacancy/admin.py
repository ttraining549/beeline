from django.contrib import admin
from .models import Vacancy
# Register your models here.


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('position', 'level', 'status')