from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import blogapi.views

urlpatterns = [
    path('', blogapi.views.home, name='home'),
    path('blogapi/create_card_post', blogapi.views.card_and_photo_upload, name='create-card-post'),
    path('blogapi/photo_upload/', blogapi.views.card_and_photo_upload, name='photo-upload'),
    path('blogapi/album_photos/', blogapi.views.album_photos, name='album-photos'),
    path('blogapi/<int:card_id>/edit_card/', blogapi.views.edit_card, name='edit-card'),
    path('blogapi/<int:card_id>/delete_card/', blogapi.views.delete_card, name='delete-card'),
    path('blogapi/<int:card_id>', blogapi.views.card_view, name='card_view'),
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
    path('blogapi/p12/', blogapi.views.display_project_13, name='p13'),
    path('blogapi/p12/', blogapi.views.display_project_14, name='p14'),
    path('blogapi/p12/', blogapi.views.display_project_15, name='p15'),
    path('blogapi/todo/', blogapi.views.todo_display, name='todo-display'),
    path('blogapi/add_todo/', blogapi.views.todo_create, name='todo-create'),
    path('blogapi/add_todo/<int:id_item>', blogapi.views.todo_create, name='todo-create'),
    path('blogapi/todo_delete/<int:id_item>', blogapi.views.todo_delete, name='todo-delete'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""Valable uniquement en developpement, avec DEBUG=True,
    MEDIA_URL est l'URL depuis laquelle Django va essayer de servir des medias.
    MEDIA_ROOT indique le répertoire local dans lequel seront sauvegardées les
    images téléversées."""
