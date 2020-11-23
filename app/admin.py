from django.contrib import admin
from app.models import *

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Article)
admin.site.register(Item)
admin.site.register(Game)
admin.site.register(Console)
admin.site.register(Review)
admin.site.register(Tag)

