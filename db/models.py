import datetime

from django.db import models
from django.db.models import DO_NOTHING
from django.db.models.fields import CharField


class Race(models.Model):
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(unique=True, max_length=255)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)


class Guild(models.Model):
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField(null=True)


class Player(models.Model):
    nickname = models.CharField(unique=True, max_length=255)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=DO_NOTHING)
    guild = models.ForeignKey(Guild, on_delete=DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)