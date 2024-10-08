import uuid
from django.db import models
from django.contrib.auth.models import User

class CarItems(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    model_number = models.CharField(max_length=100)
    user_reviews = models.TextField(max_length=500)
    image_url = models.URLField(max_length=500, null=True, blank=True)

