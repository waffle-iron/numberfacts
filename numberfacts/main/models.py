# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Number(models.Model):
    """a number"""
    number = models.IntegerField(blank=False, db_index=True, unique=True)
    created_at = models.DateTimeField(editable=False, blank=True)
    def save(self, *args, **kwargs):
        now = timezone.now()
        if not self.id:
            self.created_at = now
        return super(Number, self).save(*args, **kwargs)
    def __unicode__(self):
        return "# %s" % self.number
    def facts(self):
        return Fact.objects.filter(number = self)

class Fact(models.Model):
    """a single Fact aabout a Number"""
    number = models.ForeignKey(Number, blank=False)
    fact = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(editable=False, blank=True)
    updated_at = models.DateTimeField(editable=False, blank=True)
    user_handle = models.CharField(max_length=255, null=True, blank=True)
    approved = models.BooleanField(default=False, db_index=True)
    def save(self, *args, **kwargs):
        now = timezone.now()
        if not self.id:
            self.created_at = now
        self.updated_at = now
        return super(Fact, self).save(*args, **kwargs)
    def __unicode__(self):
        if self.approved is True:
            approved_text = "Approved"
        else:
            approved_text = "un-Approved"
        return "%s : %s [%s]" % (self.number.number, self.fact, approved_text)
