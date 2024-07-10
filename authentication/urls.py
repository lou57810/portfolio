from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
import authentication.views
import blogapi.views

from . import views