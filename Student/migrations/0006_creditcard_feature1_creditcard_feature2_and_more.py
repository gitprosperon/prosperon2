# Generated by Django 4.1.4 on 2023-02-01 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0005_creditcard_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditcard',
            name='feature1',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='creditcard',
            name='feature2',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='creditcard',
            name='feature3',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='creditcard',
            name='feature4',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='score',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
