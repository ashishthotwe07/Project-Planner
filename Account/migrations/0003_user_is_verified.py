# Generated by Django 4.2.11 on 2024-04-24 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_onetimepassword'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
