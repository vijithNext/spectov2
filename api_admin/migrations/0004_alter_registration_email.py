# Generated by Django 3.2.4 on 2021-06-09 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_admin', '0003_auto_20210609_0643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]