# Generated by Django 5.1.6 on 2025-02-22 00:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_time', models.DateTimeField()),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('registered_users', models.ManyToManyField(blank=True, related_name='registered_events', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
