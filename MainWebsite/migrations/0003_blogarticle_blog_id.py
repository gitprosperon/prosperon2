# Generated by Django 4.1.4 on 2023-02-09 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainWebsite', '0002_blogarticle_page_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogarticle',
            name='blog_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
