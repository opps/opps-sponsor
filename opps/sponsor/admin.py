# -*- encoding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from opps.core.admin import apply_opps_rules, PublishableAdmin
from opps.images.generate import image_url

from .models import Sponsor, Campaign, CampaignContainer, CampaignChannel, CampaignContainerBox


@apply_opps_rules('sponsor')
class SponsorAdmin(admin.ModelAdmin):
    model = Sponsor
    list_display = ('name', 'description')


class CampaignContainerInline(admin.TabularInline):
    model = CampaignContainer
    raw_id_fields = ['container']


class CampaignChannelInline(admin.TabularInline):
    model = CampaignChannel
    raw_id_fields = ['channel']

class CampaignContainerBoxInline(admin.TabularInline):
    model = CampaignContainerBox
    raw_id_fields = ['box']


@apply_opps_rules('sponsor')
class CampaignAdmin(PublishableAdmin):
    model = Campaign
    inlines = [CampaignContainerInline, CampaignChannelInline, CampaignContainerBoxInline]
    list_display = ('sponsor', 'name', 'show_image', 'published')
    list_filter = ('sponsor__name', 'name', 'published')

    def show_image(self, obj):
        image = obj.logo.archive
        return u'<img width="100px" height="100px" src="{0}" />'.format(
            image_url(image.url, width=100, height=100)
        )
    show_image.short_description = u'Logo da Campanha'
    show_image.allow_tags = True

    raw_id_fields = ['containers', 'logo', 'sponsor', 'top_image']
    fieldsets = (
        (_(u'Campaign'), {'fields': (
            'sponsor', 'name', 'logo', 'top_image', 'published',
            ('date_available', 'date_end'),
        )}),
        (_(u'Optional'), {'fields': (
            'cssclass', 'style', 'keyword'
        ), 'classes': ('collapse',)}),
    )

admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(Campaign, CampaignAdmin)
