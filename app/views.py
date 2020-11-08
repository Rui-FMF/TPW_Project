from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from app.forms import SignUpForm

# Create your views here.


def home(request):
    return render(request, 'index.html', {})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def articles(request):
    return render(request, 'articles.html', {})


def article_details(request, article_id):
    return render(request, 'article_details.html', {})


def create_article(request):
    return render(request, 'article_form.html', {})


def edit_article(request, article_id):
    return render(request, 'article_form.html', {})


def create_game(request):
    params = {
    }
    return render(request, 'game_form.html', params)


def edit_game(request, game_id):
    params = {
    }
    return render(request, 'game_form.html', params)


def shop_cart(request):
    return render(request, 'shop_cart.html', {})

