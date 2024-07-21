from django.contrib import admin

# Register your models here.
from blogapi.models import Photo, Blog, Article, MementoItems
from .models import User


admin.site.register(User)
admin.site.register(Photo)
admin.site.register(Blog)
admin.site.register(Article)
admin.site.register(MementoItems)
