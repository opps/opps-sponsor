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


class CampaignContainerInline(admin.StackedInline):
    model = CampaignContainer
    raw_id_fields = ['container', 'logo', 'top_image']
    extra = 1

class CampaignChannelInline(admin.StackedInline):
    model = CampaignChannel
    raw_id_fields = ['channel', 'logo', 'top_image']
    extra = 1

class CampaignContainerBoxInline(admin.StackedInline):
    model = CampaignContainerBox
    raw_id_fields = ['box', 'logo', 'top_image']
    extra = 1

@apply_opps_rules('sponsor')
class CampaignAdmin(PublishableAdmin):
    model = Campaign
    inlines = [CampaignContainerInline, CampaignChannelInline, CampaignContainerBoxInline]
    list_display = ('sponsor', 'name', 'show_image', 'published')
    list_filter = ('sponsor__name', 'name', 'published')

    def show_image(self, obj):
        if not obj.logo:
            return "No Image"

        image = obj.logo.archive
        return u'<img width="100px" height="100px" src="{0}" />'.format(
            image_url(image.url, width=100, height=100)
        )
    show_image.short_description = u'Logo da Campanha'
    show_image.allow_tags = True

    raw_id_fields = ['containers', 'logo', 'sponsor', 'top_image']
    fieldsets = (
        (_(u'Campaign'), {'fields': (
            'sponsor', 'name',
            'logo', 'top_image', 'ads_tag',
            'published',
            ('date_available', 'date_end'),
        )}),
        (_(u'Optional'), {'fields': (
            'cssclass', 'style', 'keyword'
        ), 'classes': ('collapse',)}),
    )

admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(Campaign, CampaignAdmin)
