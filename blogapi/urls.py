from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# import authentication.views
import blogapi.views

urlpatterns = [
    # path('login/', authentication.views.LoginPage.as_view(), name='login'),
    # path('logout', authentication.views.logout_user, name='logout'),
    path('', blogapi.views.home, name='home'),
    path('blogapi/photo_upload/', blogapi.views.photo_upload, name='photo_upload'),
    # path('profile-photo/upload', authentication.views.upload_profile_photo, name='upload_profile_photo'),
    path('blogapi/memento/', blogapi.views.memento_display, name='memento_display'),
    path('blogapi/add_memento/', blogapi.views.memento_create, name='memento_create'),
    path('blogapi/add_memento/<int:id_item>', blogapi.views.memento_create, name='memento_create'),
    path('blogapi/delete_memento/<int:id_item>', blogapi.views.delete_memento, name='delete_memento'),
    path('blogapi/p1/', blogapi.views.display_project_1, name='p1'),
    path('blogapi/p2/', blogapi.views.display_project_2, name='p2'),
    path('blogapi/p3/', blogapi.views.display_project_3, name='p3'),
    path('blogapi/p4/', blogapi.views.display_project_4, name='p4'),
    path('blogapi/p5/', blogapi.views.display_project_5, name='p5'),
    path('blogapi/p6/', blogapi.views.display_project_6, name='p6'),
    path('blogapi/p7/', blogapi.views.display_project_7, name='p7'),
    path('blogapi/p8/', blogapi.views.display_project_8, name='p8'),
    path('blogapi/p9/', blogapi.views.display_project_9, name='p9'),
    path('blogapi/p10/', blogapi.views.display_project_10, name='p10'),
    path('blogapi/p11/', blogapi.views.display_project_11, name='p11'),
    path('blogapi/p12/', blogapi.views.display_project_12, name='p12'),
    path('blogapi/todo/', blogapi.views.display_todo, name='todo'),
    path('blogapi/create_article/', blogapi.views.create_article, name='create-article'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)