from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__ (self):
        return f'{self.user} — {self.image}'

class Character(models.Model):
    name = models.CharField(max_length=50, unique=True)
    race = models.CharField(max_length=50)
    level = models.IntegerField(default=1, null=True, blank=True)
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    attack = models.IntegerField()
    initiative = models.IntegerField()
    hit_points = models.IntegerField()

    def save(self, *args, **kwargs):
        self.attack = int(self.strength) * 1.5
        self.hit_points = int(self.constitution) * 10
        self.initiative = int(self.dexterity) * 10
        super().save(*args, **kwargs)

    def __str__ (self):
        return self.name
    
class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=50)
    dungeon_master= models.BooleanField(default=False)
    character = models.OneToOneField(Character, on_delete=models.CASCADE, null=True, blank=True)

    def __str__ (self):
            return self.user.username

class Enemy(models.Model):
    name = models.CharField(max_length=50)
    race = models.CharField(max_length=50)
    level = models.IntegerField()
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    attack = models.IntegerField()
    atk_mod = models.FloatField()
    initiative = models.IntegerField()
    hit_points = models.IntegerField()
    
    def save(self, *args, **kwargs):
        this_strength = int(self.strength)
        this_constitution = int(self.constitution)
        this_dexterity = int(self.dexterity)
        self.attack = round(int(this_strength) * float(self.atk_mod))
        self.hit_points = int(this_constitution) * 10
        self.initiative = int(this_dexterity) * 10
        super().save(*args, **kwargs)

    def __str__ (self):
        return self.name

class Dungeon(models.Model):
    name = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=50)
    floors = models.IntegerField()
    exp = models.IntegerField()
    gold = models.IntegerField()

    def __str__ (self):
        return self.name