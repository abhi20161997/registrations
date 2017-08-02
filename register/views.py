# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
def index(request):
	return HttpResponse("WELCOME TO BITS BOSM-2017")
# Create your views here.
