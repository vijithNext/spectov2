# Generated by Django 3.2.8 on 2021-10-10 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_admin', '0046_auto_20211010_0649'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='phone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]