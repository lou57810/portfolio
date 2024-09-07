from django.shortcuts import render, redirect, get_object_or_404
# from itertools import chain
# from django.forms import formset_factory
from django.contrib.auth.decorators import login_required  # , permission_required
# from django.db.models import Q
# from django.views.generic import View
from . import forms, models

# Create your views here.


def home(request):
    photos = models.Photo.objects.all()
    return render(request, 'blogapi/home.html', context={'photos': photos})


def memento_display(request):
    # item_name alpha display.
    memento_items = models.MementoItems.objects.all().order_by('item_name')
    item_form = forms.ItemForm()

    context = {'item_form': item_form, 'memento_items': memento_items}
    return render(request, 'blogapi/memento.html', context=context)


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
    photos = models.Photo.objects.all()
    return render(request, 'blogapi/photo_upload.html', context={'form': form})


"""
def photo_delete(request, id):
    photo = Photos.objects.get(id=id)  # nécessaire pour GET et pour POST

    if request.method == 'POST':
        # supprimer le groupe de la base de données
        photo.delete()
        # rediriger vers la liste des groupes
        return redirect('photo-upload')

    return render(request,
                    'blogapi/photo_delete.html',
                    {'photo': photo})
"""
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
    context = {'delete_form': delete_form,}
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
    # articles = models.Article.objects.all()
    return render(request, 'blogapi/p1.html')


def display_project_2(request):
    # articles = models.Article.objects.all()
    return render(request, 'blogapi/p2.html')


def display_project_3(request):
    # articles = models.Article.objects.all()
    return render(request, 'blogapi/p3.html')


def display_project_4(request):
    # articles = models.Article.objects.all()
    return render(request, 'blogapi/p4.html')


def display_project_5(request):
    # articles = models.Article.objects.all()
    return render(request, 'blogapi/p5.html')


def display_project_6(request):
    # articles = models.Article.objects.all()
    return render(request, 'blogapi/p6.html')


def display_project_7(request):
    # articles = models.Article.objects.all()
    return render(request, 'blogapi/p7.html')


def display_project_8(request):
    # articles = models.Article.objects.all()
    return render(request, 'blogapi/p8.html')


def display_project_9(request):
    # articles = models.Article.objects.all()
    return render(request, 'blogapi/p9.html')


def display_project_10(request):
    # articles = models.Article.objects.all()
    return render(request, 'blogapi/p10.html')


def display_project_11(request):
    # articles = models.Article.objects.all()

    """
    followed_users_list = []
    for user in UserFollows.objects.filter(user=request.user):
        followed_users_list.append(user.followed_user)

    reviews = Review.objects.filter(
        Q(user=request.user) | Q(user__in=followed_users_list))

    tickets = Ticket.objects.filter(
            Q(user=request.user) | Q(user__in=followed_users_list)).exclude(review__in=reviews)

    ordered_tickets_and_reviews = sorted(
        chain(tickets, reviews),
        key=lambda instance: instance.time_created, reverse=True)
    
    # articles = models.Article.objects.all()
    # ordered_articles = chain(articles)

    paginator = Paginator(ordered_articles, 4)
    page = request.GET.get('page')
    page_post = paginator.get_page(page)
    """
    return render(request, 'blogapi/p11.html')  # context={'page_post': page_post})


def display_project_12(request):
    # articles = models.Article.objects.all()
    return render(request, 'blogapi/p12.html')


@login_required
def display_todo(request):
    # articles = models.Article.objects.all()
    return render(request, 'blogapi/todo.html')


@login_required
def create_article(request):
    if request.method == "GET":
        article_form = forms.ArticleForm()
        return render(request, 'blogapi/create_article.html', context={'article_form': article_form})

    if request.method == "POST":
        article_form = forms.ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            new_article = article_form.save(commit=False)
            new_article.user = request.user
            new_article.save()
            return redirect('home')
