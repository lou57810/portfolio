# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required  # , permission_required
from django.db.models.functions import Lower

from . import forms, models


def home(request):
    photos = models.Photo.objects.all()
    return render(request, 'blogapi/home.html', context={'photos': photos})


def memento_display(request):
    memento_items = models.MementoItems.objects.all().order_by(Lower('item_name'))
    item_form = forms.ItemForm()
    context = {'item_form': item_form, 'memento_items': memento_items}
    return render(request, 'blogapi/memento.html', context=context)


# @permission_required('blog.add_memento', raise_exception=True)
@login_required
def memento_create(request, id_item=None):
    instance_item = models.MementoItems.objects.get(pk=id_item) if id_item is not None else None
    if request.method == 'GET':
        item_form = forms.ItemForm(instance=instance_item)
        context = {'item_form': item_form}
        return render(request, 'blogapi/add_memento.html', context=context)
    if request.method == 'POST':
        item_form = forms.ItemForm(request.POST, instance=instance_item)
        if item_form.is_valid():
            # mem_item = item_form.save()
            item_form.save()
            return redirect('../memento')


@login_required
def delete_memento(request, id_item):
    memento = get_object_or_404(models.MementoItems, pk=id_item)
    memento.delete()
    # messages.success(request, "Memento supprimé.")
    return redirect('../memento')


# ALBUM PHOTO
@login_required
def album_photos(request):
    # photos = models.Card.objects.all()
    cards = models.Card.objects.all()
    # return render(request, 'blogapi/album_photos.html', context={'photos': photos})
    return render(request, 'blogapi/album_photos.html', context={'cards': cards})


@login_required
def photo_upload(request):
    form = forms.PhotoForm()

    if request.method == 'POST':
        form = forms.PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)  # Pour ne pas sauvegarder dans la db
            # set the uploader to the user before saving the model
            photo.uploader = request.user
            # now we can save
            photo.save()
            return redirect('home')
    # photos = models.Photo.objects.all()
    return render(request, 'blogapi/photo_upload.html', context={'form': form})


def delete_card(request, card_id):
    print('card_id:', card_id)
    card = get_object_or_404(models.Card, id=card_id)
    print('cardl:', card)
    # edit_form = forms.CardForm(instance=card)
    delete_form = forms.DeleteCardForm()
    if request.method == 'POST':
        if 'delete_card' in request.POST:
            delete_form = forms.DeleteCardForm(request.POST)
            if delete_form.is_valid():
                card.delete()
                return redirect('album-photos')
    context = {'delete_form': delete_form, }
    return render(request, 'blogapi/delete_card.html', context=context)


@login_required
def card_and_photo_upload(request):
    card_form = forms.CardForm()
    photo_form = forms.PhotoForm()
    if request.method == 'POST':
        card_form = forms.CardForm(request.POST)
        photo_form = forms.PhotoForm(request.POST, request.FILES)
        if all([card_form.is_valid(), photo_form.is_valid()]):
            photo = photo_form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            card = card_form.save(commit=False)
            card.author = request.user
            card.photo = photo
            card.save()
            return redirect('album-photos')
    # photos = models.Photo.objects.all()
    # cards = models.Blog.objects.all()
    context = {
        'card_form': card_form,
        'photo_form': photo_form,
        }
    return render(request, 'blogapi/create_card_post.html', context=context)


@login_required
def card_view(request, card_id):
    card = get_object_or_404(models.Card, id=card_id)
    return render(request, 'blogapi/card_view.html', {'card': card})


@login_required
def edit_card(request, card_id):

    card = get_object_or_404(models.Card, id=card_id)
    edit_form = forms.CardForm(instance=card)
    delete_form = forms.DeleteCardForm()
    if request.method == 'POST':
        if 'display_card' in request.POST:
            edit_form = forms.CardForm(request.POST, instance=card)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('album-photos')
            """
            if 'delete_card' in request.POST:
                delete_form = forms.DeleteCardForm(request.POST)
                if delete_form.is_valid():
                    card.delete()
                    return redirect('home')
            """
    context = {
        'card': card,
        'edit_form': edit_form,
        'delete_form': delete_form,
        }
    return render(request, 'blogapi/edit_card.html', context=context)


def display_project_1(request):
    return render(request, 'blogapi/p1.html')


def display_project_2(request):
    return render(request, 'blogapi/p2.html')


def display_project_3(request):
    return render(request, 'blogapi/p3.html')


def display_project_4(request):
    return render(request, 'blogapi/p4.html')


def display_project_5(request):
    return render(request, 'blogapi/p5.html')


def display_project_6(request):
    return render(request, 'blogapi/p6.html')


def display_project_7(request):
    return render(request, 'blogapi/p7.html')


def display_project_8(request):
    return render(request, 'blogapi/p8.html')


def display_project_9(request):
    return render(request, 'blogapi/p9.html')


def display_project_10(request):
    return render(request, 'blogapi/p10.html')


def display_project_11(request):
    return render(request, 'blogapi/p11.html')


def display_project_12(request):
    return render(request, 'blogapi/p12.html')


def display_project_13(request):
    return render(request, 'blogapi/p13.html')


def display_project_14(request):
    return render(request, 'blogapi/p14.html')


def display_project_15(request):
    return render(request, 'blogapi/p15.html')


def display_project_16(request):
    return render(request, 'blogapi/p16.html')


def display_project_17(request):
    return render(request, 'blogapi/p17.html')


def display_project_18(request):
    return render(request, 'blogapi/p18.html')


def display_contacts(request):
    return render(request, 'blogapi/contacts.html')


def display_params(request):
    return render(request, 'blogapi/params.html')


def display_favoris(request):
    return render(request, 'blogapi/favoris.html')


@login_required
def todo_display(request):
    todo_items = models.TodoItems.objects.all().order_by('TODO')
    todo_form = forms.TodoForm()

    context = {'todo_form': todo_form, 'todo_items': todo_items}
    return render(request, 'blogapi/todo.html', context=context)


@login_required
def todo_create(request, id_item=None):
    instance_item = models.TodoItems.objects.get(pk=id_item) if id_item is not None else None

    if request.method == "GET":
        todo_form = forms.TodoForm(instance=instance_item)
        context = {'todo_form': todo_form}
        return render(request, 'blogapi/add_todo.html', context=context)

    if request.method == "POST":
        todo_form = forms.TodoForm(request.POST, instance=instance_item)
        if todo_form.is_valid():
            todo_form.save()
            return redirect('../todo')


@login_required
def todo_delete(request, id_item):
    todo = get_object_or_404(models.TodoItems, pk=id_item)
    todo.delete()
    return redirect('../todo')
