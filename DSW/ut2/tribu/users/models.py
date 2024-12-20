from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to='uploads')
    bio = models.TextField(blank=True, max_length=500)

    def __str__(self):
        return self.user
