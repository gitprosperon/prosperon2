# Generated by Django 4.1.4 on 2023-03-08 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainWebsite', '0009_tool'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogarticle',
            name='date_published',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
