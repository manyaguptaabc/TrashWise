from django.contrib import admin
from .models import UserProfile, Location, WasteEntry

admin.site.register(UserProfile)
admin.site.register(Location)
admin.site.register(WasteEntry)
