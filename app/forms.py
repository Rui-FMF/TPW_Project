from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from app.models import *


class LoginForm(AuthenticationForm):
    # error_messages = {
    #     'invalid_login': (
    #         "Please enter a correct username and password. Note that both "
    #         "fields may be case-sensitive."
    #     )
    # }

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})


class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.',
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'email@example.com'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Confirm Password'})


class ArticleForm(forms.Form):
    name = forms.CharField(max_length=70, label="*Title",
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    shipping_fee = forms.DecimalField(max_value=1000000000000, decimal_places=2, label="Shipping Fee",
                                      widget=forms.NumberInput(attrs={'class': 'form-control'}))

    shipping_time = forms.ChoiceField(choices=Article.SHIPPING_TIME_CHOICES, label="*Shipping Time",
                                      widget=forms.Select(attrs={'class': 'form-control'}))


class ItemForm(forms.Form):
    price = forms.DecimalField(max_digits=1000000000000, decimal_places=2,
                               widget=forms.NumberInput(attrs={'class': 'form-control'}))
    name = forms.CharField(max_length=70,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))

    condition = models.CharField(
        max_length=1,
        choices=Item.CONDITION_CHOICES,
    )


class GameForm(forms.Form):
    price = forms.DecimalField(max_value=1000000000000, decimal_places=2, label="*Price",
                               widget=forms.NumberInput(attrs={'class': 'form-control'}))
    name = forms.CharField(max_length=70, label="*Title",
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    release_year = forms.DecimalField(max_value=2050, decimal_places=0, label="*Release Year",
                                      widget=forms.NumberInput(attrs={'class': 'form-control'}))
    publisher = forms.CharField(max_length=70, label="*Publisher",
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    genre = forms.CharField(max_length=70, label="*Genre",
                            widget=forms.TextInput(attrs={'class': 'form-control'}))

    condition = forms.ChoiceField(choices=Game.CONDITION_CHOICES, label="*Condition",
                                  widget=forms.Select(attrs={'class': 'form-control'}))
    rating = forms.ChoiceField(choices=Game.RATING_CHOICES, label="*Rating",
                               widget=forms.Select(attrs={'class': 'form-control'}))
    platform = forms.ChoiceField(choices=Game.PLATFORM_CHOICES, label="*Platform",
                                 widget=forms.Select(attrs={'class': 'form-control'}))
