# Generated by Django 5.0.3 on 2024-03-29 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cronicas', '0012_alter_avatar_image_alter_avatar_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='image',
            field=models.ImageField(blank=True, default='img/who.jpeg', null=True, upload_to='avatares'),
        ),
    ]
