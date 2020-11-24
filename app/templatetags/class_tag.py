from django import template
register = template.Library()


@register.filter(name='is_game')
def is_game(value):
    if hasattr(value, 'game'):
        return True
    else:
        return False
