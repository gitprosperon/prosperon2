# Generated by Django 4.1.4 on 2023-01-30 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0056_alter_student_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(blank=True, choices=[('Female', 'Female'), ('Male', 'Male'), ('Not Specified', 'Not Specified')], max_length=20, null=True),
        ),
    ]