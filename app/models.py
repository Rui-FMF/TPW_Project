from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    username = models.CharField(max_length=70)
    password = models.CharField(max_length=70)
    email = models.EmailField()

    def __str__(self):
        return self.username


class Article(models.Model):
    name = models.CharField(max_length=70)
    total_price = models.DecimalField(max_digits=None, decimal_places=2)
    ShippingFee = models.DecimalField(max_digits=None, decimal_places=2, default=0.00)
    Date_Posted = models.DateField().auto_now_add  # used to calculate expected delivery along with duration

    ONE = 1
    THREE = 3
    FIVE = 5
    TEN = 10
    DURATION_CHOICES = [
        (ONE, 1),
        (THREE, 3),
        (FIVE, 5),
        (TEN, 10),
    ]

    duration = models.IntegerField(
        choices=DURATION_CHOICES,
        default=TEN,
    )

    Is_sold = models.BooleanField(default=False)
    times_viewed = models.IntegerField()

    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name


class Item(models.Model):
    id = models.AutoField()
    price = models.DecimalField(max_digits=None, decimal_places=2)
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

    pertaining_article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Game(Item):
    release_year = models.DecimalField(max_digits=5, decimal_places=None)
    publisher = models.CharField(max_length=70)
    genre = models.CharField(max_length=70)
    platform = models.CharField(max_length=70)

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
    OTHER = 'OT'
    PLATFORM_CHOICES = [
        (PS4, 'Playstation 4'),
        (XBOX1, 'Xbox One'),
        (SWITCH, 'Nintendo Switch'),
        (PC, 'Computer'),
        (OTHER, 'Other'),
    ]
    platform = models.CharField(
        max_length=2,
        choices=PLATFORM_CHOICES,
        default=OTHER,
    )

    def __str__(self):
        return self.name

