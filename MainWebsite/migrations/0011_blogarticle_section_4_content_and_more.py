# Generated by Django 4.1.4 on 2023-03-10 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainWebsite', '0010_blogarticle_date_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogarticle',
            name='section_4_content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogarticle',
            name='section_4_title',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='blogarticle',
            name='section_5_content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogarticle',
            name='section_5_title',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
