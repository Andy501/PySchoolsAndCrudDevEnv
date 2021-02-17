from django.contrib import admin
from .models import MemberStudent, BehaviorGrade

# Register your models here.

@admin.register(MemberStudent)
class StudentsAdmin(admin.ModelAdmin):
    #list_display = ('name', 'instructor',)
    #prepopulated_fields = {"slug":("name",)}#how d
    pass

@admin.register(BehaviorGrade)
class StudentBehaviorAdmin(admin.ModelAdmin):
    pass