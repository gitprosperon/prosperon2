# Generated by Django 4.1.4 on 2023-03-19 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Budget', '0005_budgetusers_average_income'),
    ]

    operations = [
        migrations.AddField(
            model_name='budgetusers',
            name='credit_avaliable',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
