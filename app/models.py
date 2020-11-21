from django.db import models
from django.contrib.auth.models import User
# Create your models here.

"""
class User(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    username = models.CharField(max_length=70)
    password = models.CharField(max_length=70)
    email = models.EmailField()

    def __str__(self):
        return self.username
"""


class Article(models.Model):
    name = models.CharField(max_length=70)
    total_price = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)
    ShippingFee = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)
    Date_Posted = models.DateField().auto_now_add  # used to calculate expected delivery along with duration

    ONE = 1
    THREE = 3
    FIVE = 5
    TEN = 10
    SHIPPING_TIME_CHOICES = [
        (ONE, '1 day'),
        (THREE, '3 days'),
        (FIVE, '5 days'),
        (TEN, '10 days'),
    ]

    ShippingTime = models.IntegerField(
        choices=SHIPPING_TIME_CHOICES,
        default=TEN,
    )

    Is_sold = models.BooleanField(default=False)
    times_viewed = models.IntegerField(default=0)

    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Articles_posted")
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None, related_name="Articles_bought")

    def __str__(self):
        return self.name


class Item(models.Model):
    price = models.DecimalField(max_digits=13, decimal_places=2)
    name = models.CharField(max_length=70)

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
    condition = models.CharField(
        max_length=1,
        choices=CONDITION_CHOICES,
        default=BRAND_NEW,
    )

    pertaining_article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="items_in_article")

    def __str__(self):
        return self.name


class Game(Item):
    release_year = models.DecimalField(max_digits=5, decimal_places=0)
    publisher = models.CharField(max_length=70)
    genre = models.CharField(max_length=70)

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
    rating = models.CharField(
        max_length=1,
        choices=RATING_CHOICES,
        default=EVERYONE,
    )

    PS4 = 'PS'
    XBOX1 = 'XB'
    SWITCH = 'SW'
    PC = 'PC'
    WII = 'WI'
    RETRO = 'RT'
    PLATFORM_CHOICES = [
        (PS4, 'Playstation'),
        (XBOX1, 'Xbox One'),
        (SWITCH, 'Nintendo'),
        (PC, 'Computer'),
        (WII, 'Wii'),
        (RETRO, 'Retro'),
    ]
    platform = models.CharField(
        max_length=2,
        choices=PLATFORM_CHOICES,
        blank=True,
    )
    # Difference between blank and null:
    # https://simpleisbetterthancomplex.com/tips/2016/07/25/django-tip-8-blank-or-null.html

    def __str__(self):
        return self.name


class Console(Item):
    release_year = models.DecimalField(max_digits=5, decimal_places=0)
    brand = models.CharField(max_length=70)
    storage_capacity = models.CharField(max_length=20)
    color = models.CharField(max_length=70)

    def __str__(self):
        return self.name



