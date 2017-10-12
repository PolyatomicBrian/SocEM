# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Identity
from forms import IdentityForm

def index(request):
    """Render index page."""
    context = {}
    return render(request, 'index.html', context)

def identities(request):
    """Render identities page."""
    # Check if user is submitting something.
    if request.POST:
        # User is creating new Identity.
        if 'create' in request.POST:
            create_identity(request)
    context = {}
    # Get all identities from db.
    identity_list = Identity.objects.all()
    # If list not empty, add to context.
    if identity_list:
        context['identities'] = identity_list
    context['form'] = IdentityForm()
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

def create_identity(request):
    """Parses info from POST request and stores in db."""
    # User didn't POST any data, so we can't create anything.
    if not request.POST:
        return
    # User submitted an email and a password, so save them to an Identity.
    if 'email' and 'password' in request.POST:
        email = request.POST['email']
        password = request.POST['password']
        new_identity = Identity.objects.create(email=email, password=password)
        try:
            new_identity.save()
            print '[*] Saving new Identity %s' % new_identity
        except Exception as e:
            print '[!] Unable to save Identity! %s' % e
