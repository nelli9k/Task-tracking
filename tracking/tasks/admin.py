from django.contrib import admin
from .models import Task

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "due_to", "assigned_to")
    search_fields = ("title", "description")
    list_filter = ("status", "assigned_to")