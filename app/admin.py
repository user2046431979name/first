from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(News)
admin.site.register(NewsImages)
admin.site.register(Gallery)
admin.site.register(NewsDetails)
admin.site.register(Comments)