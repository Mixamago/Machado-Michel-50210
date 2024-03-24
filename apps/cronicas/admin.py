from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Player)

admin.site.register(Avatar)

admin.site.register(Character)

admin.site.register(Enemy)

admin.site.register(Dungeon)