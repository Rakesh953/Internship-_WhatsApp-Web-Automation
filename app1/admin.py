from django.contrib import admin

# Register your models here.
from app1.models import *

admin.site.register(Usermessages)
admin.site.register(profile)
admin.site.register(user_status)