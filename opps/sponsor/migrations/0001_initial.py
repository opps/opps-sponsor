# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Sponsor'
        db.create_table(u'sponsor_sponsor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'sponsor', ['Sponsor'])

        # Adding model 'Campaign'
        db.create_table(u'sponsor_campaign', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_insert', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['%s.%s' % (User._meta.app_label, User._meta.object_name)])),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['sites.Site'])),
            ('site_iid', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True, max_length=4, null=True, blank=True)),
            ('site_domain', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=100, null=True, blank=True)),
            ('date_available', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, db_index=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('visibility', self.gf('django.db.models.fields.CharField')(default='post', max_length=20)),
            ('sponsor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sponsor.Sponsor'])),
            ('logo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['images.Image'], null=True, blank=True)),
            ('top_image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='campaigntopimage', null=True, to=orm['images.Image'])),
            ('ads_tag', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('date_end', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('cssclass', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('style', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('keyword', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'sponsor', ['Campaign'])

        # Adding model 'CampaignContainer'
        db.create_table(u'sponsor_campaigncontainer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('campaign', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sponsor.Campaign'])),
            ('container', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['containers.Container'])),
            ('logo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['images.Image'], null=True, blank=True)),
            ('top_image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='campaigncontainertopimage', null=True, to=orm['images.Image'])),
            ('ads_tag', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'sponsor', ['CampaignContainer'])

        # Adding model 'CampaignContainerBox'
        db.create_table(u'sponsor_campaigncontainerbox', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('campaign', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sponsor.Campaign'])),
            ('box', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['containers.ContainerBox'])),
            ('logo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['images.Image'], null=True, blank=True)),
            ('top_image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='campaigncontainerboxtopimage', null=True, to=orm['images.Image'])),
            ('ads_tag', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'sponsor', ['CampaignContainerBox'])

        # Adding model 'CampaignChannel'
        db.create_table(u'sponsor_campaignchannel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('campaign', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sponsor.Campaign'])),
            ('channel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['channels.Channel'])),
            ('logo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['images.Image'], null=True, blank=True)),
            ('top_image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='campaignchanneltopimage', null=True, to=orm['images.Image'])),
            ('ads_tag', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'sponsor', ['CampaignChannel'])


    def backwards(self, orm):
        # Deleting model 'Sponsor'
        db.delete_table(u'sponsor_sponsor')

        # Deleting model 'Campaign'
        db.delete_table(u'sponsor_campaign')

        # Deleting model 'CampaignContainer'
        db.delete_table(u'sponsor_campaigncontainer')

        # Deleting model 'CampaignContainerBox'
        db.delete_table(u'sponsor_campaigncontainerbox')

        # Deleting model 'CampaignChannel'
        db.delete_table(u'sponsor_campaignchannel')


    models = {
        u'%s.%s' % (User._meta.app_label, User._meta.module_name): {
            'Meta': {'object_name': User.__name__},
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'boxes.queryset': {
            'Meta': {'object_name': 'QuerySet'},
            'channel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['channels.Channel']", 'null': 'True', 'blank': 'True'}),
            'date_available': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'db_index': 'True'}),
            'date_insert': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'filters': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limit': ('django.db.models.fields.PositiveIntegerField', [], {'default': '7'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'order': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['sites.Site']"}),
            'site_domain': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'site_iid': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True', 'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '150'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['%s.%s']" % (User._meta.app_label, User._meta.object_name)})
        },
        u'channels.channel': {
            'Meta': {'ordering': "['name', 'parent__id', 'published']", 'unique_together': "(('site', 'long_slug', 'slug', 'parent'),)", 'object_name': 'Channel'},
            'date_available': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'db_index': 'True'}),
            'date_insert': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'homepage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'include_in_main_rss': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'layout': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '250', 'db_index': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'long_slug': ('django.db.models.fields.SlugField', [], {'max_length': '250'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'subchannel'", 'null': 'True', 'to': u"orm['channels.Channel']"}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'show_in_menu': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['sites.Site']"}),
            'site_domain': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'site_iid': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True', 'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['%s.%s']" % (User._meta.app_label, User._meta.object_name)})
        },
        u'containers.container': {
            'Meta': {'ordering': "['-date_available']", 'unique_together': "(('site', 'channel_long_slug', 'slug'),)", 'object_name': 'Container'},
            'channel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['channels.Channel']"}),
            'channel_long_slug': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'channel_name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'child_app_label': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'child_class': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'child_module': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'date_available': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'db_index': 'True'}),
            'date_insert': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'hat': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['images.Image']", 'null': 'True', 'through': u"orm['containers.ContainerImage']", 'blank': 'True'}),
            'json': ('opps.db.models.fields.jsonf.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'main_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'containers_container_mainimage'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['images.Image']"}),
            'main_image_caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'polymorphic_containers.container_set'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'show_on_root_channel': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['sites.Site']"}),
            'site_domain': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'site_iid': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True', 'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '4000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140', 'db_index': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['%s.%s']" % (User._meta.app_label, User._meta.object_name)})
        },
        u'containers.containerbox': {
            'Meta': {'object_name': 'ContainerBox'},
            'channel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['channels.Channel']"}),
            'channel_long_slug': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'channel_name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'containers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'containerbox_containers'", 'to': u"orm['containers.Container']", 'through': u"orm['containers.ContainerBoxContainers']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'date_available': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'db_index': 'True'}),
            'date_insert': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'queryset': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'containerbox_querysets'", 'null': 'True', 'to': u"orm['boxes.QuerySet']"}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['sites.Site']"}),
            'site_domain': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'site_iid': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True', 'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '150'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['%s.%s']" % (User._meta.app_label, User._meta.object_name)})
        },
        u'containers.containerboxcontainers': {
            'Meta': {'ordering': "('order', 'aggregate')", 'object_name': 'ContainerBoxContainers'},
            'aggregate': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'container': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['containers.Container']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'containerbox': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['containers.ContainerBox']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'date_available': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True'}),
            'date_end': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'hat': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'highlight': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_image': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['images.Image']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'main_image_caption': ('django.db.models.fields.CharField', [], {'max_length': '4000', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'containers.containerimage': {
            'Meta': {'ordering': "('order',)", 'object_name': 'ContainerImage'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'container': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['containers.Container']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['images.Image']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'images.image': {
            'Meta': {'object_name': 'Image'},
            'archive': ('django.db.models.fields.files.FileField', [], {'max_length': '255'}),
            'crop_example': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'crop_x1': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'crop_x2': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'crop_y1': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'crop_y2': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'date_available': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'db_index': 'True'}),
            'date_insert': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fit_in': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'flip': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'flop': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'halign': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '6', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['sites.Site']"}),
            'site_domain': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'site_iid': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True', 'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150'}),
            'smart': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '4000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140', 'db_index': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['%s.%s']" % (User._meta.app_label, User._meta.object_name)}),
            'valign': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '6', 'null': 'True', 'blank': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'sponsor.campaign': {
            'Meta': {'object_name': 'Campaign'},
            'ads_tag': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'boxes': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['containers.ContainerBox']", 'through': u"orm['sponsor.CampaignContainerBox']", 'symmetrical': 'False'}),
            'channels': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['channels.Channel']", 'through': u"orm['sponsor.CampaignChannel']", 'symmetrical': 'False'}),
            'containers': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['containers.Container']", 'through': u"orm['sponsor.CampaignContainer']", 'symmetrical': 'False'}),
            'cssclass': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'date_available': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'db_index': 'True'}),
            'date_end': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_insert': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyword': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'logo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['images.Image']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['sites.Site']"}),
            'site_domain': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'site_iid': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True', 'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'sponsor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sponsor.Sponsor']"}),
            'style': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'top_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'campaigntopimage'", 'null': 'True', 'to': u"orm['images.Image']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['%s.%s']" % (User._meta.app_label, User._meta.object_name)}),
            'visibility': ('django.db.models.fields.CharField', [], {'default': "'post'", 'max_length': '20'})
        },
        u'sponsor.campaignchannel': {
            'Meta': {'object_name': 'CampaignChannel'},
            'ads_tag': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sponsor.Campaign']"}),
            'channel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['channels.Channel']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['images.Image']", 'null': 'True', 'blank': 'True'}),
            'top_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'campaignchanneltopimage'", 'null': 'True', 'to': u"orm['images.Image']"})
        },
        u'sponsor.campaigncontainer': {
            'Meta': {'object_name': 'CampaignContainer'},
            'ads_tag': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sponsor.Campaign']"}),
            'container': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['containers.Container']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['images.Image']", 'null': 'True', 'blank': 'True'}),
            'top_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'campaigncontainertopimage'", 'null': 'True', 'to': u"orm['images.Image']"})
        },
        u'sponsor.campaigncontainerbox': {
            'Meta': {'object_name': 'CampaignContainerBox'},
            'ads_tag': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'box': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['containers.ContainerBox']"}),
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sponsor.Campaign']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['images.Image']", 'null': 'True', 'blank': 'True'}),
            'top_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'campaigncontainerboxtopimage'", 'null': 'True', 'to': u"orm['images.Image']"})
        },
        u'sponsor.sponsor': {
            'Meta': {'object_name': 'Sponsor'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['sponsor']