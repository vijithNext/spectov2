# Generated by Django 3.0.7 on 2021-10-12 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_admin', '0068_auto_20211012_0721'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Attachment',
        ),
        migrations.DeleteModel(
            name='DefaultFiles',
        ),
        migrations.DeleteModel(
            name='ImageUpload',
        ),
        migrations.RemoveField(
            model_name='labour',
            name='login_user',
        ),
        migrations.DeleteModel(
            name='TaskAssign',
        ),
        migrations.DeleteModel(
            name='Ticket',
        ),
        migrations.DeleteModel(
            name='Labour',
        ),
    ]