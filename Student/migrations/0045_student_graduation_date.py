# Generated by Django 4.1.4 on 2023-02-07 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0044_student_current_net_worth'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='graduation_date',
            field=models.CharField(blank=True, choices=[('Spring_2023', 'Spring 2023')], max_length=200, null=True),
        ),
    ]