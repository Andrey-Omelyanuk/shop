# -*- coding: utf-8 -*-
from django.db.models   import Model, CASCADE, ForeignKey, CharField, TextField, DateTimeField, BooleanField, IntegerField
from django.contrib.postgres.fields import JSONField


class Smartphone(Model):
    title = CharField(max_length=256, unique=True)

    def __str__(self):
        return self.title

