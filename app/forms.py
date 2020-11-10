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
    ShippingFee = forms.DecimalField(max_value=10000000000, decimal_places=2, label="Shipping Fee")
    ONE = 1
    THREE = 3
    FIVE = 5
    TEN = 10
    SHIPPINGTIME_CHOICES = [
        (ONE, 1),
        (THREE, 3),
        (FIVE, 5),
        (TEN, 10),
    ]
    ShippingTime = forms.ChoiceField(choices=SHIPPINGTIME_CHOICES, label="*Shipping Time")


class ItemForm(forms.Form):
    ...


class GameForm(forms.Form):
    price = forms.DecimalField(max_value=10000000000, decimal_places=2, label="*Price")
    name = forms.CharField(max_length=70, label="*Title")
    release_year = forms.DecimalField(max_value=2050, decimal_places=0, label="*Release Year")
    publisher = forms.CharField(max_length=70, label="*Publisher")
    genre = forms.CharField(max_length=70, label="*Genre")

    BRAND_NEW = 'B'
    LIKE_NEW = 'L'
    VERY_GOOD = 'V'
    GOOD = 'G'
    ACCEPTABLE = 'A'
    CONDITION_CHOICES = [
        (BRAND_NEW, 'Brand New'),
        (LIKE_NEW, 'Like New'),
        (VERY_GOOD, 'Very Good'),
        (GOOD, 'Good'),
        (ACCEPTABLE, 'Acceptable'),
    ]
    EVERYONE = 'E'
    TEEN = 'T'
    MATURE = 'M'
    ADULT = 'A'
    RATING_CHOICES = [
        (EVERYONE, 'Everyone'),
        (TEEN, 'Teen'),
        (MATURE, 'Mature'),
        (ADULT, 'Adult'),
    ]
    PS4 = 'PS'
    XBOX1 = 'XB'
    SWITCH = 'SW'
    PC = 'PC'
    OTHER = 'OT'
    PLATFORM_CHOICES = [
        (PS4, 'Playstation 4'),
        (XBOX1, 'Xbox One'),
        (SWITCH, 'Nintendo Switch'),
        (PC, 'Computer'),
        (OTHER, 'Other'),
    ]

    condition = forms.ChoiceField(choices=CONDITION_CHOICES, label="*Condition")
    rating = forms.ChoiceField(choices=RATING_CHOICES, label="*Rating")
    platform = forms.ChoiceField(choices=PLATFORM_CHOICES, label="*Platform")

