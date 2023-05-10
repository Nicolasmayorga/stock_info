from django.contrib import admin
from .models import User, APILog

admin.site.register(User)
admin.site.register(APILog)
