# Generated by Django 5.0.3 on 2024-03-29 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cronicas', '0005_alter_avatar_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='characters',
            field=models.BooleanField(default=False),
        ),
    ]