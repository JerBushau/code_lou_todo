from django.contrib import admin

from . import models

# Adds data model to the admin panel
admin.site.register(models.Todo)
