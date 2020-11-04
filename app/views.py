from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html', {})


def login(request):
    return render(request, 'login.html', {})


def signup(request):
    return render(request, 'signup.html', {})


def articles(request):
    return render(request, 'articles.html', {})


def article_details(request, article_id):
    return render(request, 'article_details.html', {})


def create_article(request):
    return render(request, 'article_form.html', {})


def edit_article(request, article_id):
    return render(request, 'article_form.html', {})


def create_game(request):
    return render(request, 'game_form.html', {})


def edit_game(request, game_id):
    return render(request, 'game_form.html', {})


def shop_cart(request):
    return render(request, 'shop_cart.html', {})

