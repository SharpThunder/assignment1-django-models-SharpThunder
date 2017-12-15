# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Singer(models.Model):
    name = models.CharField(max_length=30)

class Album(models.Model):
    menu = models.ForeignKey(Singer)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
