# Generated by Django 4.1.3 on 2022-11-25 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0012_room_active_bots'),
    ]

    operations = [
        migrations.AddField(
            model_name='bot',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
