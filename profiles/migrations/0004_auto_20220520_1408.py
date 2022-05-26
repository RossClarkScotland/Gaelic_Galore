# Generated by Django 3.2.13 on 2022-05-20 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_rename_default_phone_userprofile_default_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_address',
            new_name='default_street_address1',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='default_street_address2',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]