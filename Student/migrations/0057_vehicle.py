# Generated by Django 4.1.4 on 2023-02-08 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0056_alter_monthlyexpense_monthly_expense_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_title', models.CharField(blank=True, max_length=400, null=True)),
            ],
        ),
    ]
