# -*- encoding: utf-8 -*-
from django import models
from django.utils.translation import ugettext_lazy as _

from opps.articles.models import Article
from opps.images.models import Image

class Sponsor(models.Model):
    name = models.CharField(_(u'Sponsor Name'), max_length=255)
    description = models.TextField(_(u'Description'), blank=True)

    __unicode__ = lambda self: self.name

    class Meta:
        verbose_name = _(u'Sponsor')
        verbose_name_plural = _(u'Sponsors')

class Campaign(Article):
    sponsor = models.ForeignKey('sponsor.Sponsor')
    logo = models.ForeignKey(Image, verbose_name=_(u'Logo'))
    posts = models.ManyToManyField(
        'articles.Post',
        through='CampaignPost',
        verbose_name='campaign',
    )

    class Meta:
        verbose_name=_(u'Campaign')
        verbose_name_plural=_(u'Campaigns')

class CampaignPost(models.Model):
     campaign = models.ForeignKey('sponsor.Campaign',
                                  on_delete=models.SET_NULL)
     post = models.ForeignKey('articles.Post', on_delete=models.SET_NULL)
