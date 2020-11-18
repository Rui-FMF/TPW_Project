from app.forms import LoginForm


def login(request):
    kwargs = {
        'login_form': LoginForm(),
    }
    if request.method == 'POST':
        if 'login' in request.POST:
            if not LoginForm(request.POST).is_valid():
                kwargs['login_form'] = LoginForm(request.POST)
                kwargs['login_error'] = True
    return kwargs
