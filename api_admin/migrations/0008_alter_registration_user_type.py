# Generated by Django 3.2.4 on 2021-06-09 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_admin', '0007_alter_registration_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='user_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
