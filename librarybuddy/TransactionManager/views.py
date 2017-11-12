# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from silk.profiling.profiler import silk_profile


@silk_profile
def details(request, *args, **kwargs):
    pass
