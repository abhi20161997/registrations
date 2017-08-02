# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class Team_Captain(models.Model):
 	name=models.CharField(max_length=200)
 	email_id=models.EmailField(max_length=200)
	def __str__(self):
 		return self.name

class Team_member(models.Model):
	Team_Captain=models.ForeignKey(Team_Captain,on_delete=models.CASCADE)
	member_name=models.CharField(max_length=200)