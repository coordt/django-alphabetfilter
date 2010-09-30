"""
This file unregisters the admin class for each model specified in 
ALPHAFILTER_ADMIN_FIELDS and replaces it with a new admin class that 
subclasses both the original admin and one with an alphabet_filter attribute
"""

from django.db.models import get_model
from django.contrib import admin
from django.conf import settings

MODEL_REGISTRY = getattr(settings, 'ALPHAFILTER_ADMIN_FIELDS', {})
FIELDS = {}

for key, val in MODEL_REGISTRY.items():
    if isinstance(key, basestring):
        FIELDS[get_model(*key.split('.'))] = val


for model, modeladmin in admin.site._registry.items():
    if model in FIELDS:
        admin.site.unregister(model)
        admin.site.register(model, type('newadmin', (modeladmin.__class__,), {
            'alphabet_filter': FIELDS[model],
        }))