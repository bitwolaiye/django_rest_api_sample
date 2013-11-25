# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Follow'
        db.create_table('pet_follow', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pet.User'])),
            ('follow_user_id', self.gf('django.db.models.fields.IntegerField')()),
            ('follow_time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('pet', ['Follow'])

        # Adding model 'Info'
        db.create_table('pet_info', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pet.User'])),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('pic_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('pet', ['Info'])

        # Adding model 'Fan'
        db.create_table('pet_fan', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pet.User'])),
            ('fan_user_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('pet', ['Fan'])

        # Adding model 'News'
        db.create_table('pet_news', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pet.User'])),
            ('news_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('news_desc', self.gf('django.db.models.fields.CharField')(max_length=400)),
        ))
        db.send_create_signal('pet', ['News'])

        # Adding model 'Feed'
        db.create_table('pet_feed', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pet.User'])),
            ('info', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pet.Info'])),
            ('feed_ts', self.gf('django.db.models.fields.BigIntegerField')()),
            ('feed_user_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('pet', ['Feed'])

        # Adding model 'Comment'
        db.create_table('pet_comment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pet.User'])),
            ('info', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pet.Info'])),
            ('comment_note', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('comment_time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('pet', ['Comment'])

        # Adding model 'Friend'
        db.create_table('pet_friend', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pet.User'])),
            ('friend_user_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('pet', ['Friend'])

        # Adding field 'User.gender'
        db.add_column('pet_user', 'gender',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'User.avatar'
        db.add_column('pet_user', 'avatar',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Adding field 'User.follow_cnt'
        db.add_column('pet_user', 'follow_cnt',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'User.fan_cnt'
        db.add_column('pet_user', 'fan_cnt',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'User.friend_cnt'
        db.add_column('pet_user', 'friend_cnt',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Follow'
        db.delete_table('pet_follow')

        # Deleting model 'Info'
        db.delete_table('pet_info')

        # Deleting model 'Fan'
        db.delete_table('pet_fan')

        # Deleting model 'News'
        db.delete_table('pet_news')

        # Deleting model 'Feed'
        db.delete_table('pet_feed')

        # Deleting model 'Comment'
        db.delete_table('pet_comment')

        # Deleting model 'Friend'
        db.delete_table('pet_friend')

        # Deleting field 'User.gender'
        db.delete_column('pet_user', 'gender')

        # Deleting field 'User.avatar'
        db.delete_column('pet_user', 'avatar')

        # Deleting field 'User.follow_cnt'
        db.delete_column('pet_user', 'follow_cnt')

        # Deleting field 'User.fan_cnt'
        db.delete_column('pet_user', 'fan_cnt')

        # Deleting field 'User.friend_cnt'
        db.delete_column('pet_user', 'friend_cnt')


    models = {
        'pet.comment': {
            'Meta': {'object_name': 'Comment'},
            'comment_note': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'comment_time': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pet.Info']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pet.User']"})
        },
        'pet.fan': {
            'Meta': {'object_name': 'Fan'},
            'fan_user_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pet.User']"})
        },
        'pet.feed': {
            'Meta': {'object_name': 'Feed'},
            'feed_ts': ('django.db.models.fields.BigIntegerField', [], {}),
            'feed_user_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pet.Info']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pet.User']"})
        },
        'pet.follow': {
            'Meta': {'object_name': 'Follow'},
            'follow_time': ('django.db.models.fields.DateTimeField', [], {}),
            'follow_user_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pet.User']"})
        },
        'pet.friend': {
            'Meta': {'object_name': 'Friend'},
            'friend_user_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pet.User']"})
        },
        'pet.info': {
            'Meta': {'object_name': 'Info'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pic_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pet.User']"})
        },
        'pet.news': {
            'Meta': {'object_name': 'News'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'news_desc': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'news_time': ('django.db.models.fields.DateTimeField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pet.User']"})
        },
        'pet.user': {
            'Meta': {'object_name': 'User'},
            'avatar': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'fan_cnt': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'follow_cnt': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'friend_cnt': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gender': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['pet']