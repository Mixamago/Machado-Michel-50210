from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class PlayerForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    country = forms.CharField(max_length=50, help_text='Obligatorio.')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'country')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        player = Player(user=user, country=self.cleaned_data['country'])
        if commit:
            player.save()
        return user

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'race', 'level', 'strength', 'dexterity', 'constitution', 'intelligence']

class EnemyForm(forms.ModelForm):
    class Meta:
        model = Enemy
        fields = ['name', 'race', 'level', 'strength', 'dexterity', 'constitution', 'intelligence', 'atk_mod']

class DungeonForm(forms.ModelForm):
    class Meta:
        model = Dungeon
        fields = ['name', 'difficulty', 'floors', 'exp', 'gold']

class EditForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label= "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label= "Repetir la contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    country = forms.CharField(max_length=50)    

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2', 'country')

    def save(self, commit=True):
        self.clean()
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        player = Player.objects.get(user=user)
        player.country = self.cleaned_data['country']
        if commit:
            player.save()
        return user
    
class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ["image"]