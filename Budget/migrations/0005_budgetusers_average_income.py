# Generated by Django 4.1.4 on 2023-03-19 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Budget', '0004_budgetusers_checking_savings_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='budgetusers',
            name='average_income',
            field=models.FloatField(blank=True, null=True),
        ),
    ]