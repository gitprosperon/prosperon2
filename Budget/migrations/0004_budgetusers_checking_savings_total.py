# Generated by Django 4.1.4 on 2023-03-19 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Budget', '0003_budgetusers'),
    ]

    operations = [
        migrations.AddField(
            model_name='budgetusers',
            name='checking_savings_total',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
