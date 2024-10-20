# Generated by Django 5.1.2 on 2024-10-18 18:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('due_to', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('to_do', 'To do'), ('in_progress', 'In Progress'), ('completed', 'Completed')], default='to_do', max_length=20)),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
