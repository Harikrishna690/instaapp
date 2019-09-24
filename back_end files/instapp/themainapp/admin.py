from django.contrib import admin

# Register your models here.
from .models import User, Comments, Images, Liked

# Register your models here.
admin.site.register(User)
admin.site.register(Comments)
admin.site.register(Images)
admin.site.register(Liked)
