# Generated by Django 4.1.4 on 2023-02-11 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0067_student_apartments'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='properties',
            field=models.JSONField(blank=True, null=True),
        ),
    ]