# Generated by Django 4.1.4 on 2023-02-09 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainWebsite', '0003_blogarticle_blog_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogarticle',
            name='blog_id',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
