# Generated by Django 3.2.4 on 2021-06-09 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_admin', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='first_name',
            new_name='mobile_number',
        ),
        migrations.RenameField(
            model_name='registration',
            old_name='last_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='registration',
            name='dup_password',
            field=models.CharField(max_length=255, null=True),
        ),
    ]