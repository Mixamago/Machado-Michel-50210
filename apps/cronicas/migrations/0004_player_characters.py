# Generated by Django 5.0.3 on 2024-03-25 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cronicas', '0003_player_dungeon_master'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='characters',
            field=models.IntegerField(default=0),
        ),
    ]
