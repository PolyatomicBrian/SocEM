# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# Identity Class
class Identity(models.Model):
    """Model for Identity."""
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return "%s" % self.email


# Email Class
class Email(models.Model):
    """Model for Email."""
    subject = models.CharField(max_length=255)
    header = models.CharField(max_length=255)
    content = models.TextField()
    signature = models.CharField(max_length=255)

    def __str__(self):
        return "%s" % self.subject
