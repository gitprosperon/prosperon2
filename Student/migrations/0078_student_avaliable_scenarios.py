# Generated by Django 4.1.4 on 2023-03-07 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0077_scenario'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='avaliable_scenarios',
            field=models.CharField(blank=True, max_length=900, null=True),
        ),
    ]