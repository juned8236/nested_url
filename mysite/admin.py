from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Sport)
admin.site.register(Market)
admin.site.register(Selection)
admin.site.register(Match)


