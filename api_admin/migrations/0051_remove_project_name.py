# Generated by Django 3.2.5 on 2021-10-10 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_admin', '0050_alter_project_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='name',
        ),
    ]
