# Generated by Django 4.1.4 on 2023-01-31 01:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0065_student_yearly_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='job',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Student.job'),
        ),
    ]