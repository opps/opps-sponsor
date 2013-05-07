# -*- encoding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from opps.core.admin import apply_opps_rules, PublishableAdmin
from django_thumbor import generate_url

from .models import Sponsor, Campaign, CampaignPost, CampaignChannel


@apply_opps_rules('sponsor')
class SponsorAdmin(admin.ModelAdmin):
    model = Sponsor
    list_display = ('name', 'description')


class CampaignPostInline(admin.TabularInline):
    model = CampaignPost
    raw_id_fields = ['post']


class CampaignChannelInline(admin.TabularInline):
    model = CampaignChannel
    raw_id_fields = ['channel']


@apply_opps_rules('sponsor')
class CampaignAdmin(PublishableAdmin):
    model = Campaign
    inlines = [CampaignPostInline, CampaignChannelInline]
    list_display = ('sponsor', 'name', 'show_image', 'published')
    list_filter = ('sponsor__name', 'name', 'published')

    def show_image(self, obj):
        print type(obj.logo.image)
        image = obj.logo.image
        return u'<img width="100px" height="100px" src="{0}" />'.format(
            generate_url(image.url, width=100, height=100)
        )
    show_image.short_description = u'Logo da Campanha'
    show_image.allow_tags = True

    raw_id_fields = ['posts', 'logo', 'sponsor']
    fieldsets = (
        (_(u'Campaign'), {'fields': (
            'sponsor', 'name', 'logo', 'published',
            ('date_available', 'date_end'),
            'visibility'
        )}),
        (_(u'Optional'), {'fields': (
            'cssclass', 'style', 'keyword'
        ), 'classes': ('collapse',)}),
    )

admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(Campaign, CampaignAdmin)
