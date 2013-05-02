# -*- encoding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from opps.core.admin import apply_opps_rules

from .models import Sponsor, Campaign, CampaignPost

@apply_opps_rules('sponsor')
class SponsorAdmin(admin.ModelAdmin):
    model = Sponsor
    list_display = ('name', 'description')

class CampaignPostInline(admin.TabularInline):
    model = CampaignPost
    raw_id_fields = ['post']

@apply_opps_rules('sponsor')
class CampaignAdmin(admin.ModelAdmin):
    model = Campaign
    inlines = [CampaignPostInline]

    raw_id_fields = ['posts', 'logo']
    fieldsets = (
        (_(u'Campaign'), {'fields': ('sponsor', 'logo')}),
    )

admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(Campaign, CampaignAdmin)
