# Generated by Django 4.1.4 on 2023-02-02 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0020_alter_anytimedecision_back_btn_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='budgetitemsuniversity',
            name='transactions',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
