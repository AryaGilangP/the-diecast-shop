from django.db import models

class MoodEntry(models.Model):
    name = models.CharField(max_length=70)
    price = models.IntegerField()
    description = models.TextField(max_length=2000)
    model_number = models.IntegerField()
    user_reviews = models.TextField(max_length=1000)

# buat push baru