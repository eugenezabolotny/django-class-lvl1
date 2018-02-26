# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from flake8.formatting import default


class Todo(models.Model):
    text = models.CharField(max_length=40)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text
