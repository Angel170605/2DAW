from django.conf import settings
from django.db import models


class Echo(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='user', on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
