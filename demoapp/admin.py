from django.contrib import admin

from . models import *

# Register your models here.

admin.site.register(morning)
admin.site.register(afternoon)
admin.site.register(evening)
admin.site.register(employee)