# Generated by Django 5.0.3 on 2024-03-24 01:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dungeon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('difficulty', models.CharField(max_length=50)),
                ('floors', models.IntegerField()),
                ('exp', models.IntegerField()),
                ('gold', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Enemy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('race', models.CharField(max_length=50)),
                ('level', models.IntegerField()),
                ('strength', models.IntegerField()),
                ('dexterity', models.IntegerField()),
                ('constitution', models.IntegerField()),
                ('intelligence', models.IntegerField()),
                ('attack', models.IntegerField()),
                ('atk_mod', models.IntegerField(default=1)),
                ('initiative', models.IntegerField()),
                ('hit_points', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='avatares')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('race', models.CharField(max_length=50)),
                ('level', models.IntegerField(default=1)),
                ('strength', models.IntegerField()),
                ('dexterity', models.IntegerField()),
                ('constitution', models.IntegerField()),
                ('intelligence', models.IntegerField()),
                ('attack', models.IntegerField()),
                ('initiative', models.IntegerField()),
                ('hit_points', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('country', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]