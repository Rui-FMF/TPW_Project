from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm
from django.core.files.images import get_image_dimensions   # python3.9 -m pip install --upgrade Pillow
from app.models import *


class LoginForm(AuthenticationForm):
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


class SettingsForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(SettingsForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Old Password'})
        self.fields['new_password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'New Password'})
        self.fields['new_password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Confirm New Password'})


class UserForm(UserChangeForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.',
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'email@example.com'}))

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)


class UserProfileForm(forms.ModelForm):
    biography = forms.CharField(max_length=2000, required=False, help_text='Optional.',
                                widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = UserProfile
        fields = ('avatar', 'biography',)

    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']
        try:
            w, h = get_image_dimensions(avatar)
            # validate dimensions
            max_width = max_height = 500
            if w != h:
                raise forms.ValidationError(
                    'Please use an image with proportion 1:1.')
            if w > max_width or h > max_height:
                raise forms.ValidationError(
                    u'Please use an image that is '
                     '%s x %s pixels or smaller.' % (max_width, max_height))
            # validate content type
            main, sub = avatar.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, '
                    'GIF or PNG image.')
            # validate file size
            if len(avatar) > (100 * 1024):
                raise forms.ValidationError(
                    u'Avatar file size may not exceed 100k.')
        except AttributeError:
            """
            Handles case when we are updating the user profile
            and do not supply a new avatar
            """
            pass
        return avatar


class ReviewForm(forms.Form):
    rate = forms.IntegerField(max_value=5, min_value=0)
    message = forms.CharField(max_length=2000, required=False)


class ArticleForm(forms.Form):
    name = forms.CharField(max_length=70, label="*Title",
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    ShippingFee = forms.DecimalField(max_value=1000000000000, decimal_places=2, label="Shipping Fee",
                                      widget=forms.NumberInput(attrs={'class': 'form-control'}))

    ShippingTime = forms.ChoiceField(choices=Article.SHIPPING_TIME_CHOICES, label="*Shipping Time",
                                      widget=forms.Select(attrs={'class': 'form-control'}))

    description = forms.CharField(max_length=2000, required=False, label="Description", widget=forms.Textarea(attrs={"rows": 6}))


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


class ConsoleForm(forms.Form):
    price = forms.DecimalField(max_value=1000000000000, decimal_places=2, label="*Price",
                               widget=forms.NumberInput(attrs={'class': 'form-control'}))
    name = forms.CharField(max_length=70, label="*Title",
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    release_year = forms.DecimalField(max_value=2050, decimal_places=0, label="*Release Year",
                                      widget=forms.NumberInput(attrs={'class': 'form-control'}))
    brand = forms.CharField(max_length=70, label="*Brand",
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    storage_capacity = forms.CharField(max_length=20, label="*Storage",
                                       widget=forms.TextInput(attrs={'class': 'form-control'}))
    color = forms.CharField(max_length=70, label="*Color",
                            widget=forms.TextInput(attrs={'class': 'form-control'}))

    condition = forms.ChoiceField(choices=Console.CONDITION_CHOICES, label="*Condition",
                                  widget=forms.Select(attrs={'class': 'form-control'}))
