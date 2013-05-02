# -*- encoding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from opps.images.models import Image

class Sponsor(models.Model):
    name = models.CharField(_(u'Nome'), max_length=255)
    description = models.TextField(_(u'Descrição'), blank=True)

    __unicode__ = lambda self: self.name

    class Meta:
        verbose_name = _(u'Patrocinador')
        verbose_name_plural = _(u'Patrocinadores')

class Campaign(models.Model):
    name = models.CharField(u'Nome da Campanha', max_length=255, blank=True)
    sponsor = models.ForeignKey('sponsor.Sponsor')
    logo = models.ForeignKey(Image, verbose_name=_(u'Logo'))
    posts = models.ManyToManyField(
        'articles.Post',
        through='CampaignPost',
        verbose_name='campaign',
    )

    __unicode__ = lambda self: self.name or self.sponsor.name

    class Meta:
        verbose_name=_(u'Campanha')
        verbose_name_plural=_(u'Campanhas')

class CampaignPost(models.Model):
     campaign = models.ForeignKey('sponsor.Campaign')
     post = models.ForeignKey('articles.Post')
