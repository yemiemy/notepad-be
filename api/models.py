from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(null=True,  blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.body[:50]

    class Meta:
        ordering = ['-updated']