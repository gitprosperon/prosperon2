# Generated by Django 4.1.4 on 2023-02-09 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='demo',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
