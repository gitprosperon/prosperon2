# Generated by Django 4.1.4 on 2023-03-15 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0086_student_desired_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='general_information',
            field=models.TextField(blank=True, max_length=50000, null=True),
        ),
    ]
