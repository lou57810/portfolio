from itertools import chain

from django.contrib.auth.decorators import login_required, permission_required
from django.forms import formset_factory
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View
from django.core.paginator import Paginator

from . import forms, models


@login_required
def photo_upload(request):
    form = forms.PhotoForm()
    if request.method == 'POST':
        form = forms.PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False) # Pour ne pas sauvegarder dans la db
            # set the uploader to the user before saving the model
            photo.uploader = request.user
            # now we can save
            photo.save()
            return redirect('home')
        return render(request, 'blogapi/photo_upload.html', context={'form': form})


# @login_required
def dashboard(request):
    photos = models.Photo.objects.all()
    return render(request, 'blogapi/dashboard.html', context={'photos': photos})


@login_required
def memento_create(request, id_item=None):
    # item_form = forms.ItemForm()
    instance_item = models.MementoItems.objects.get(pk=id_item) if id_item is not None else None
    if request.method == 'GET':
        item_form = forms.ItemForm(instance=instance_item)
        context = {'item_form': item_form}
        return render(request, 'blogapi/add_memento.html', context=context)
    if request.method == 'POST':
        item_form = forms.ItemForm(request.POST, instance=instance_item)
        if item_form.is_valid():
            mem_item = item_form.save()
            print('mem_item:', mem_item)
            return redirect('../memento')

    # context = {'item_form': item_form, 'memento_items': memento_items}
    # return render(request, 'blogapi/add_memento.html', context=context)



@login_required
def memento_display(request):
    memento_items = models.MementoItems.objects.all()
    item_form = forms.ItemForm()

    context = {'item_form': item_form, 'memento_items': memento_items}
    return render(request, 'blogapi/memento.html', context=context)



@login_required
def delete_memento(request, id_item):
    memento = get_object_or_404(models.MementoItems, pk=id_item)
    memento.delete()
    # messages.success(request, "Memento supprimé.")
    return redirect('../memento')

# =============== Articles pages ==============

@login_required
def display_project_1(request):
    articles = models.Article.objects.all()
    return render(request, 'blogapi/p1.html')


@login_required
def display_project_2(request):
    articles = models.Article.objects.all()
    return render(request, 'blogapi/p2.html')


@login_required
def display_project_3(request):
    articles = models.Article.objects.all()
    return render(request, 'blogapi/p3.html')


@login_required
def display_project_4(request):
    articles = models.Article.objects.all()
    return render(request, 'blogapi/p4.html')


@login_required
def display_project_5(request):
    articles = models.Article.objects.all()
    return render(request, 'blogapi/p5.html')


@login_required
def display_project_6(request):
    articles = models.Article.objects.all()
    return render(request, 'blogapi/p6.html')


@login_required
def display_project_7(request):
    articles = models.Article.objects.all()
    return render(request, 'blogapi/p7.html')


@login_required
def display_project_8(request):
    articles = models.Article.objects.all()
    return render(request, 'blogapi/p8.html')


@login_required
def display_project_9(request):
    articles = models.Article.objects.all()
    return render(request, 'blogapi/p9.html')


@login_required
def display_project_10(request):
    articles = models.Article.objects.all()
    return render(request, 'blogapi/p10.html')

@login_required
def display_project_11(request):
    articles = models.Article.objects.all()

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
    """
    articles = models.Article.objects.all()
    # ordered_articles = chain(articles)
    """
    paginator = Paginator(ordered_articles, 4)
    page = request.GET.get('page')
    page_post = paginator.get_page(page)
    """
    return render(request, 'blogapi/p11.html')
                 # context={'page_post': page_post})


@login_required
def display_project_12(request):
    articles = models.Article.objects.all()
    return render(request, 'blogapi/p12.html')


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





