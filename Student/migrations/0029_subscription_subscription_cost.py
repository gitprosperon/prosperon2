# Generated by Django 4.1.4 on 2023-02-05 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0028_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='subscription_cost',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
