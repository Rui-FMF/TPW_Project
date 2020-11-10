from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app.models import *


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class ArticleForm(forms.Form):
    name = forms.CharField(max_length=70, label="*Title")
    shipping_fee = forms.DecimalField(max_value=13, decimal_places=2, label="Shipping Fee")

    shipping_time = forms.ChoiceField(choices=Article.SHIPPING_TIME_CHOICES, label="*Shipping Time")


class ItemForm(forms.Form):
    price = forms.DecimalField(max_digits=13, decimal_places=2)
    name = forms.CharField(max_length=70)

    condition = models.CharField(
        max_length=1,
        choices=Item.CONDITION_CHOICES,
    )


class GameForm(forms.Form):
    price = forms.DecimalField(max_value=13, decimal_places=2, label="*Price")
    name = forms.CharField(max_length=70, label="*Title")
    release_year = forms.DecimalField(max_value=2050, decimal_places=0, label="*Release Year")
    publisher = forms.CharField(max_length=70, label="*Publisher")
    genre = forms.CharField(max_length=70, label="*Genre")

    condition = forms.ChoiceField(choices=Game.CONDITION_CHOICES, label="*Condition")
    rating = forms.ChoiceField(choices=Game.RATING_CHOICES, label="*Rating")
    platform = forms.ChoiceField(choices=Game.PLATFORM_CHOICES, label="*Platform")

