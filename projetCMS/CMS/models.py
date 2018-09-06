# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Post(models.Model):
    post_date = models.DateTimeField(auto_now_add=True)
    post_title = models.CharField(max_length=50)
    post_content = models.CharField(max_length=5000)
    text = models.TextField(blank=True)
    picture_url = models.CharField(max_length=5000, blank=True )

    def __str__(self):
        return f' {self.post_title}'




