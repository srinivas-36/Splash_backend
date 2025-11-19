# imgbackendapp/models.py
from django.db import models


class Ornament(models.Model):
    image = models.ImageField(upload_to='uploads/')
    prompt = models.CharField(
        max_length=255, blank=True, null=True)  # ✅ allow blank
    generated_image = models.ImageField(
        upload_to='generated/', null=True, blank=True)
    # Store User ID as string since User is a MongoEngine model
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Ornament {self.id}'
