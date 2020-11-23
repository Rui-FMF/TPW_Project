from django import template
from app.models import Article, Review
from django.db.models import Avg

register = template.Library()


@register.simple_tag(takes_context=True)
def user_rating(context, user_id):
    avg_rate = Review.objects.filter(reviewed=user_id).aggregate(Avg('rate'))['rate__avg']
    return 0 if avg_rate is None else avg_rate


@register.simple_tag(takes_context=True)
def article_rating(context, article_id):
    avg_rate = Review.objects.filter(
        reviewed=Article.objects.get(id=article_id).seller.id).aggregate(Avg('rate'))['rate__avg']
    return 0 if avg_rate is None else avg_rate


@register.simple_tag(takes_context=True)
def user_reviews_number(context, article_id):
    user = Article.objects.get(id=article_id).seller
    return Review.objects.filter(reviewed=user.id).count()


@register.simple_tag(takes_context=True)
def param_replace(context, **kwargs):
    """
    Return encoded URL parameters that are the same as the current
    request's parameters, only with the specified GET parameters added or changed.

    It also removes any empty parameters to keep things neat,
    so you can remove a parm by setting it to ``""``.

    For example, if you're on the page ``/things/?with_frosting=true&page=5``,
    then

    <a href="/things/?{% param_replace page=3 %}">Page 3</a>

    would expand to

    <a href="/things/?with_frosting=true&page=3">Page 3</a>

    Based on
    https://stackoverflow.com/questions/22734695/next-and-before-links-for-a-django-paginated-query/22735278#22735278
    """
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    for k in [k for k, v in d.items() if not v]:
        del d[k]
    return d.urlencode()
