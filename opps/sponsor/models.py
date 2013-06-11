# -*- encoding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from opps.images.models import Image
from opps.core.models import Publishable


class Sponsor(models.Model):
    name = models.CharField(_(u'Name'), max_length=255)
    description = models.TextField(_(u'Description'), blank=True)

    __unicode__ = lambda self: self.name

    class Meta:
        verbose_name = _(u'Sponsor')
        verbose_name_plural = _(u'Sponsors')


class Campaign(Publishable):
    VISIBILITY = (
        ('post', _(u'Post')),
        ('channel', _(u'Channel')),
    )
    name = models.CharField(
        _(u'Campaign Name'),
        max_length=255,
        blank=True
    )
    title = models.CharField(
        _(u'Campaign Title'),
        max_length=255,
        blank=True,
        null=True
    )
    visibility = models.CharField(
        _(u'Visibility'),
        max_length=20,
        choices=VISIBILITY,
        default='post'
    )
    sponsor = models.ForeignKey('sponsor.Sponsor',
                                verbose_name=_(u'Sponsor'))
    logo = models.ForeignKey(
        Image,
        verbose_name=_(u'Logo')
    )
    posts = models.ManyToManyField(
        'articles.Post',
        through='CampaignPost',
        verbose_name=_(u'Campaign'),
    )
    channels = models.ManyToManyField(
        'channels.Channel',
        through='CampaignChannel',
        verbose_name=_(u'Channel'),
    )
    date_end = models.DateTimeField(_(u"End date"), null=True, blank=True)

    # optional fields
    cssclass = models.CharField(
        _(u"CSS class"),
        max_length=40,
        blank=True,
        null=True
    )
    style = models.CharField(
        _(u"CSS style"),
        max_length=255,
        blank=True,
        null=True
    )
    keyword = models.CharField(
        _(u"Keyword"),
        max_length=255,
        blank=True,
        null=True
    )

    __unicode__ = lambda self: self.name or self.sponsor.name

    class Meta:
        verbose_name = _(u'Campaign')
        verbose_name_plural = _(u'Campaigns')
        get_latest_by = 'date_available'


class CampaignPost(models.Model):
    campaign = models.ForeignKey('sponsor.Campaign',
                                 verbose_name=_(u'Campaign'))
    post = models.ForeignKey('articles.Post',
                             verbose_name=_(u'Post'))

    class Meta:
        verbose_name = _(u'Campaign Post')
        verbose_name_plural = _(u'Campaign Posts')

class CampaignChannel(models.Model):
    campaign = models.ForeignKey('sponsor.Campaign',
                                 verbose_name=_(u'Campaign'))
    channel = models.ForeignKey('channels.Channel',
                                verbose_name=_(u'Channel'))
    class Meta:
        verbose_name = _(u'Campaign Channel')
        verbose_name_plural = _(u'Campaign Channels')
