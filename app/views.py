from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.urls import reverse
from django.core.paginator import Paginator

from app.forms import SignupForm, ArticleForm, GameForm
from app.models import *

# Create your views here.


def home(request):
    # TODO: change to top 6 Articles most viewed
    return render(request, 'index.html', {'platforms': Game.PLATFORM_CHOICES, 'popular_articles': Article.objects.all()[:6]})


def signup(request):

    if request.method == 'POST':
        print(request.POST.get('name'))
        print(request.POST)
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})


def articles(request, article_type=None, article_platform=None):
    if article_type is not None and article_type not in ('games', 'consoles'):
        return HttpResponse(status=404)
    if article_platform is not None and article_platform not in Game.PLATFORM_CHOICES:
        return HttpResponse(status=404)
    params = {}
    form = {
        'search': '',
        'price': (0, 1200),
    }
    if request.method == 'GET':
        # apply search bar
        if all(p in request.GET for p in ('submit_search', 'search')):
            form['search'] = request.GET['search']
        # apply all
        else:
            if 'search' in request.GET:
                form['search'] = request.GET['search']
            if 'price' in request.GET:
                try:
                    form['price'] = [int(p) for p in request.GET['price'].split(',')]
                except ValueError:
                    pass
        # filter and order query to avoid warnings in paginator
        queryset = Article.objects.get_queryset().filter(
            Is_sold=False, name__icontains=form['search'],
            total_price__range=form['price']
            ).order_by("id")
        if article_type == 'games':
            queryset = [a for a in queryset if Game.objects.filter(pertaining_article=a.id).exists()]
        elif article_type == 'console':
            # queryset = [a for a in queryset if Console.objects.filter(pertaining_article=a.id).exists()] # TODO: create Console
            pass
        page_obj = Paginator(queryset, 16).page(1)
        # get page
        if 'page' in request.GET:
            try:
                page = int(request.GET['page'])
                if 1 <= page <= page_obj.paginator.num_pages:
                    page_obj = page_obj.paginator.page(page)
            except ValueError:
                pass
        params = {
            'article_type': article_type,
            'page_obj': page_obj,
            'form': form,
        }
    return render(request, 'articles.html', params)


def article_details(request, article_id):
    return render(request, 'article_details.html', {})


def create_article1(request):
    temp = Article.objects.filter(name=request.user.id)
    items = []
    if temp.count() == 0:
        a = Article(name=request.user.id, seller=request.user)
        a.save()
        price = 0
    else:
        a = temp[0]
        price = 0
        if (request.method == 'POST') and "del" in request.POST:
            iid = int(request.POST["del"])
            Item.objects.get(id=iid).delete()
        for i in a.items_in_article.all():
            items.append(i)
            price += i.price

    if request.method == 'POST' and "del" not in request.POST:
        if len(items)>0:
            return HttpResponseRedirect(reverse('create_article2'))
    return render(request, 'article_form1.html', {'items': items, 'price': str(price)})


def create_article2(request):

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            shipping_fee = form.cleaned_data['shipping_fee']
            shipping_time = form.cleaned_data['shipping_time']
            a = Article.objects.get(name=request.user.id)
            a2 = Article(name=name, ShippingFee=shipping_fee, ShippingTime=shipping_time, seller=request.user,
                         times_viewed=0)
            a2.save()
            total_price = 0
            for i in a.items_in_article.all():
                i.pertaining_article = a2
                i.save()
                total_price += i.price
            a2.total_price = total_price
            Article.objects.get(name=request.user.id).delete()
            a2.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = ArticleForm()
        a = Article.objects.filter(name=request.user.id)[0]
        items = []
        price = 0
        for i in a.items_in_article.all():
            items.append(i)
            price += i.price
    return render(request, 'article_form2.html', {'form': form, 'items': items, 'price': str(price)})


def edit_article(request, article_id):
    return render(request, 'article_form2.html', {})


def create_game(request):

    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            release_year = form.cleaned_data['release_year']
            publisher = form.cleaned_data['publisher']
            genre = form.cleaned_data['genre']
            condition = form.cleaned_data['condition']
            rating = form.cleaned_data['rating']
            platform = form.cleaned_data['platform']
            a = Article.objects.get(name=request.user.id)
            g = Game(name=name, price=price, release_year=release_year, publisher=publisher,
                     genre=genre, condition=condition, rating=rating, platform=platform, pertaining_article=a)
            g.save()
            return HttpResponseRedirect(reverse('create_article1'))
    else:
        form = GameForm()
    return render(request, 'game_form.html', {'form': form})


def edit_game(request, game_id):
    params = {}
    return render(request, 'game_form.html', params)


def shop_cart(request):
    return render(request, 'shop_cart.html', {})


def saved(request):
    # order query to avoid warnings in paginator
    page_obj = Paginator(Article.objects.get_queryset().order_by('id'), 8).page(1)
    # TODO: change to saved articles according to request.user.id
    if request.method == 'GET':
        if 'page' in request.GET:
            try:
                page = int(request.GET['page'])
                if 1 <= page <= page_obj.paginator.num_pages:
                    page_obj = page_obj.paginator.page(page)
            except ValueError:
                pass
    return render(request, 'articles_alt.html', {'page_obj': page_obj})



