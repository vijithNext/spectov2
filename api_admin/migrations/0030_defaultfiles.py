# Generated by Django 3.2.5 on 2021-07-18 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_admin', '0029_attachment'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.FileField(blank=True, max_length=5000, null=True, upload_to='default/')),
                ('status', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]