from django import template

register = template.Library()


@register.filter()
def dogs_media(val):
    if val:
        return fr'/media/{val}'
    return '/static/dummydog.jpg'


@register.filter
def class_name(obj):
    return obj.__class__.__name__
