# -*- encoding: utf-8 -*-
from django import template
from django.utils import timezone
from django.db.models import Q

register = template.Library()

# from ..models import Campaign


@register.simple_tag
def get_campaign(post,
                 template_name='sponsor/campaign.html',
                 **kwargs):
    now = timezone.now()
    lookup = dict(
        published=True,
        date_available__lte=now
    )
    # Gets published campaigns of this post
    campaign = post.campaign_set.filter(**lookup).filter(
        Q(date_end__gte=now) | Q(date_end__isnull=True)
    )
    if not campaign:
        #try to get channel campaigns
        campaign = post.channel.campaign_set.filter(**lookup).filter(
            Q(date_end__gte=now) | Q(date_end__isnull=True)
        )
    t = template.loader.get_template(template_name)

    if campaign:
        campaign = campaign.latest()

    return t.render(
        template.Context(
            {'campaign': campaign, 'post': post}
        )
    )
