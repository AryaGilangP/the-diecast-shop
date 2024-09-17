import uuid
from django.db import models

class CarItems(models.Model):
    name = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price = models.IntegerField()
    description = models.TextField(max_length=2000)
    model_number = models.IntegerField()
    user_reviews = models.TextField(max_length=1000)

