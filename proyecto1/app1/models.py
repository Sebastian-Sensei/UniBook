# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class App1(models.Model):
	description = models.CharField(max_length=128)
	is_done = models.BooleanField(default=False)
