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
        ('box', _(u'Box')),
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
        verbose_name=_(u'Logo'),
        null=True,
        blank=True
    )
    top_image = models.ForeignKey(
        Image,
        verbose_name=_(u'Top Image'),
        null=True,
        blank=True,
        related_name='campaigntopimage'
    )
    ads_tag = models.TextField(
        _(u"Ads tags"),
        null=True,
        blank=True
    )
    containers = models.ManyToManyField(
        'containers.Container',
        through='CampaignContainer',
        verbose_name=_(u'Campaign'),
    )
    channels = models.ManyToManyField(
        'channels.Channel',
        through='CampaignChannel',
        verbose_name=_(u'Channel'),
    )
    boxes = models.ManyToManyField(
        'containers.ContainerBox',
        through='CampaignContainerBox',
        verbose_name=_(u'Box')
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

    def get_containers(self):
        return self.campaigncontainer_set.all()
        
class CampaignContainer(models.Model):
    campaign = models.ForeignKey('sponsor.Campaign',
                                 verbose_name=_(u'Campaign'))
    container = models.ForeignKey('containers.Container',
                             verbose_name=_(u'Container'))
    logo = models.ForeignKey(
        Image,
        verbose_name=_(u'Logo'),
        null=True,
        blank=True
    )
    top_image = models.ForeignKey(
        Image,
        verbose_name=_(u'Top Image'),
        null=True,
        blank=True,
        related_name='campaigncontainertopimage'
    )
    ads_tag = models.TextField(
        _(u"Ads tags"),
        null=True,
        blank=True
    )

    __unicode__ = lambda self: self.container.__unicode__()
    
    class Meta:
        verbose_name = _(u'Campaign Container')
        verbose_name_plural = _(u'Campaign Containers')

class CampaignContainerBox(models.Model):
    campaign = models.ForeignKey('sponsor.Campaign',
                                 verbose_name=_(u'Campaign'))
    box = models.ForeignKey('containers.ContainerBox',
                             verbose_name=_(u'Box'))

    logo = models.ForeignKey(
        Image,
        verbose_name=_(u'Logo'),
        null=True,
        blank=True
    )
    top_image = models.ForeignKey(
        Image,
        verbose_name=_(u'Top Image'),
        null=True,
        blank=True,
        related_name='campaigncontainerboxtopimage'
    )
    ads_tag = models.TextField(
        _(u"Ads tags"),
        null=True,
        blank=True
    )

    __unicode__ = lambda self: self.box.__unicode__()

    class Meta:
        verbose_name = _(u'Campaign Box')
        verbose_name_plural = _(u'Campaign Boxes')

class CampaignChannel(models.Model):
    campaign = models.ForeignKey('sponsor.Campaign',
                                 verbose_name=_(u'Campaign'))
    channel = models.ForeignKey('channels.Channel',
                                verbose_name=_(u'Channel'))

    logo = models.ForeignKey(
        Image,
        verbose_name=_(u'Logo'),
        null=True,
        blank=True
    )
    top_image = models.ForeignKey(
        Image,
        verbose_name=_(u'Top Image'),
        null=True,
        blank=True,
        related_name='campaignchanneltopimage'
    )
    ads_tag = models.TextField(
        _(u"Ads tags"),
        null=True,
        blank=True
    )

    __unicode__ = lambda self: self.channel.__unicode__()

    class Meta:
        verbose_name = _(u'Campaign Channel')
        verbose_name_plural = _(u'Campaign Channels')
