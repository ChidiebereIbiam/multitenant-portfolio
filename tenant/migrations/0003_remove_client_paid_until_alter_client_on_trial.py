# Generated by Django 5.0.6 on 2024-06-09 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenant', '0002_remove_client_address_remove_client_name_client_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='paid_until',
        ),
        migrations.AlterField(
            model_name='client',
            name='on_trial',
            field=models.BooleanField(default=True),
        ),
    ]
