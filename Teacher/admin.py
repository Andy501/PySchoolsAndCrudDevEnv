from django.contrib import admin
from .models import Teachers

# Register your models here.

@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')
    prepopulated_fields = {"slug":("name",)}#how do add id?