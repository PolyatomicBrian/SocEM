# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def index(request):
    """Render index page."""
    context = {}
    return render(request, 'index.html', context)

def identities(request):
    """Render identities page."""
    context = {}
    return render(request, 'identities.html', context)

def profiles(request):
    """Render profiles page."""
    context = {}
    return render(request, 'profiles.html', context)

def emails(request):
    """Render emails page."""
    context = {}
    return render(request, 'emails.html', context)

def hosting(request):
    """Render hosting page."""
    context = {}
    return render(request, 'hosting.html', context)
