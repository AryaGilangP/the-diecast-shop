# Generated by Django 5.1.1 on 2024-09-22 14:31

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_caritems_delete_moodentry'),
    ]

    operations = [
        migrations.AddField(
            model_name='caritems',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='caritems',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
