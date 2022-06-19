from django import template
from django.contrib.auth.models import User
from hashlib import md5

register = template.Library()


@register.filter(name="gravatar")
def gravatar(user: User, size: int = 35) -> str:
    email = str(user.email.strip().lower()).encode("utf-8")
    email_hash = md5(email).hexdigest()
    url = "//www.gravatar.com/avatar/{0}?s={1}&d=identicon&r=PG"
    return url.format(email_hash, size)


@register.filter(name="genres")
def genres(queryset):
    return queryset.filter(parent__slug="genres")


@register.simple_tag
def url_replace(request, field, value):
    dict_ = request.GET.copy()
    dict_[field] = value
    return dict_.urlencode()