from django.db import models
from django.conf import settings
from PIL import Image


class Photo(models.Model):
    image = models.ImageField(verbose_name='image')
    caption = models.CharField(max_length=128, blank=True, verbose_name='légende')
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)


class Blog(models.Model):
    photo = models.ForeignKey(Photo, null=True, on_delete=models.SET_NULL, blank=True)
    title = models.CharField(max_length=128, verbose_name='titre')
    content = models.CharField(max_length=5000, verbose_name='contenu')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    starred = models.BooleanField(default=False)


class Article(models.Model):
    IMAGE_MAX_SIZE = (400, 400)

    title = models.CharField(max_length=128)
    description = models.TextField(max_length=16384, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(verbose_name='image', null=True, blank=True)

    def __str__(self):
        return self.title  # + ' | ' + str(self.user)

    def resize_image(self):
        try:
            image = Image.open(self.image)
            image.thumbnail(self.IMAGE_MAX_SIZE)
            image.save(self.image.path)

        except ValueError:
            print('review or ticket without image!')
            pass

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image is not None:
            self.resize_image()


class MementoItems(models.Model):
    item_name = models.CharField(max_length=128, verbose_name='item_name')
    item_explanation = models.CharField(max_length=128, verbose_name='item_explanation')

