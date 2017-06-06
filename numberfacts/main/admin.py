# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Number, Fact

admin.site.register(Number)
admin.site.register(Fact)
