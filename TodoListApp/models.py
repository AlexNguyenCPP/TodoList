from django.conf import settings
from django.db import models
from django.utils import timezone

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.title