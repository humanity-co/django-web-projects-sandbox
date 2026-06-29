from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *  # Import all models from the current app

# Register your models here.
for model in [m for m in globals().values() if hasattr(m, 'Meta')]:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass