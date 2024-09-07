from django.contrib import admin

# Register your models here.
from blogapi.models import Photo, Card, Article, MementoItems
from .models import Subscriber


admin.site.register(Subscriber)
admin.site.register(Photo)
admin.site.register(Card)
admin.site.register(Article)
admin.site.register(MementoItems)
