from django import  template


register = template.Library()


@register.filter()
def games_media(val):
    if val:
        return fr'/media/{val}'
    return '/static/images_6.jpg'


