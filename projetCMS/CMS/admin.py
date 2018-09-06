# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'post_title', 'post_date', 'post_content','text']
    list_editable = ['post_title', 'post_content','text']
    date_hierarchy = 'post_date'

