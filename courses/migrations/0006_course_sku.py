# Generated by Django 3.2.13 on 2022-05-12 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20220503_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='sku',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]