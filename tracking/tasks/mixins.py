from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from .models import Task
from django.core.exceptions import PermissionDenied

class TaskOwnerMixin(LoginRequiredMixin):
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.assigned_to != self.request.user:
            raise PermissionDenied
        return obj