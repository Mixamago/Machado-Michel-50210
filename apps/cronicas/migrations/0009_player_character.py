# Generated by Django 5.0.3 on 2024-03-29 01:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cronicas', '0008_rename_character_player_have_character'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='character',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cronicas.character'),
        ),
    ]
