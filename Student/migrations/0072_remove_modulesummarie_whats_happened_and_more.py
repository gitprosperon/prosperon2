# Generated by Django 4.1.4 on 2023-01-31 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0071_video_page_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modulesummarie',
            name='whats_happened',
        ),
        migrations.AddField(
            model_name='universitymodule',
            name='whats_happened',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
    ]
