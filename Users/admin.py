from django.contrib import admin

# Register your models here.
from .models import profile, Skill

admin.site.register(profile)
admin.site.register(Skill)