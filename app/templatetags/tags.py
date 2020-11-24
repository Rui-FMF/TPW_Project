from django import template
from app.models import Article, Review, Item, UserProfile
from django.db.models import Avg
from django.conf import settings

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
def user_rating(context, user_id):
    avg_rate = Review.objects.filter(reviewed=user_id).aggregate(Avg('rate'))['rate__avg']
    return 0 if avg_rate is None else avg_rate


@register.simple_tag(takes_context=True)
def param_replace(context, **kwargs):
    """Return encoded URL parameters that are the same as the current
    request's parameters, only with the specified GET parameters added or changed.

    It also removes any empty parameters to keep things neat,
    so you can remove a parm by setting it to ``""``.
    """
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    for k in [k for k, v in d.items() if not v]:
        del d[k]
    return d.urlencode()


@register.simple_tag(takes_context=True)
def user_img_path(context, user_id):
    if not user_id:
        return ''
    if not UserProfile.objects.filter(user_id=user_id).exists():
        return settings.MEDIA_URL + 'default_profile' + str(user_id % 4 + 1)
    return settings.MEDIA_URL + 'user_{0}/profile'.format(user_id)


@register.simple_tag(takes_context=True)
def item_img_path(context, item_id):
    if not item_id:
        return ''
    item = Item.objects.get(id=item_id)
    return settings.MEDIA_URL + 'user_{0}/article_{1}/item_{2}'.format(
        item.pertaining_article.seller.id, item.pertaining_article.id, item.id)
