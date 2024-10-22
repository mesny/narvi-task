# Generated by Django 5.1.2 on 2024-10-21 15:13

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('version', models.PositiveIntegerField(default=1, editable=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tokens', to='app_api.group')),
            ],
        ),
        # make the DB generate UUIDs, instead of the app
        # migrations.RunSQL(
        #     "ALTER TABLE app_api_group ALTER COLUMN id SET DEFAULT gen_random_uuid();"
        # ),
        # migrations.RunSQL(
        #     "ALTER TABLE app_api_token ALTER COLUMN id SET DEFAULT gen_random_uuid();"
        # ),
    ]