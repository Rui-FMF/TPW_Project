from app.forms import LoginForm, Article


def navbar(request):
    kwargs = {
        'login_form': LoginForm(),
    }
    if request.method == 'POST':
        if 'login' in request.POST:
            if not LoginForm(request.POST).is_valid():
                kwargs['login_form'] = LoginForm(request.POST)
                kwargs['login_error'] = True

    if request.user.is_authenticated:
        kwargs['articles_on_cart_total'] = Article.objects.filter(shop_cart=request.user).count()
    return kwargs
