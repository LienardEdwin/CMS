# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Post(models.Model):
    post_date = models.DateTimeField(auto_now_add=True)
    post_title = models.CharField(max_length=50)
    post_content = models.CharField(max_length=5000)
    def __str__(self):
        return f'Post {self.post_title}'
