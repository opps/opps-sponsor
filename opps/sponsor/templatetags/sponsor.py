# -*- encoding: utf-8 -*-
from django import template

register = template.Library()

from django_thumbor import generate_url

from ..models import Campaign

@register.simple_tag
def get_campaign_logo(post, **kwargs):
    width = kwargs.get('width', 100)
    height = kwargs.get('height', 100)
    try:
        # Gets the latest published campaign of this post
        campaign = post.campaign_set.all_published().latest()
    except Campaign.DoesNotExist:
        return None
    return u'<img src="{}" width="{}px" height="{}px" />'.format(
        generate_url(campaign.logo.image.url, width=width, height=height),
        width,
        height,
    )
