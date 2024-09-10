# Generated by Django 5.1.1 on 2024-09-10 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MoodEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('price', models.IntegerField()),
                ('description', models.TextField(max_length=2000)),
                ('model_number', models.IntegerField()),
                ('user_reviews', models.TextField(max_length=1000)),
            ],
        ),
    ]
