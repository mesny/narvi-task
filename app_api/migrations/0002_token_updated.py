# Generated by Django 5.1.2 on 2024-10-21 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
