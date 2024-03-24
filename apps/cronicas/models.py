from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    age = models.IntegerField()
    country = models.CharField(max_length=50)

    def __str__ (self):
            return self.user.username

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__ (self):
        return f'{self.user} — {self.image}'

class Character(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    race = models.CharField(max_length=50)
    level = models.IntegerField(default=1)
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    attack = models.IntegerField()
    initiative = models.IntegerField()
    hit_points = models.IntegerField()

    def save(self, *args, **kwargs):
        self.attack = self.strength
        self.hit_points = self.constitution * 10
        self.initiative = self.dexterity * 10
        super().save(*args, **kwargs)

    def __str__ (self):
        return self.name

class Enemy(models.Model):
    name = models.CharField(max_length=50)
    race = models.CharField(max_length=50)
    level = models.IntegerField()
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    attack = models.IntegerField()
    atk_mod = models.IntegerField(default=1)
    initiative = models.IntegerField()
    hit_points = models.IntegerField()
    
    def save(self, *args, **kwargs):
        self.attack = round(self.strength * self.atk_mod)
        self.hit_points = self.constitution * 10
        self.initiative = self.dexterity * 10
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