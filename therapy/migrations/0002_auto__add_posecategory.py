# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PoseCategory'
        db.create_table('therapy_posecategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('therapy', ['PoseCategory'])

        # Adding M2M table for field pose_category on 'Exercise'
        db.create_table('therapy_exercise_pose_category', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('exercise', models.ForeignKey(orm['therapy.exercise'], null=False)),
            ('posecategory', models.ForeignKey(orm['therapy.posecategory'], null=False))
        ))
        db.create_unique('therapy_exercise_pose_category', ['exercise_id', 'posecategory_id'])


    def backwards(self, orm):
        # Deleting model 'PoseCategory'
        db.delete_table('therapy_posecategory')

        # Removing M2M table for field pose_category on 'Exercise'
        db.delete_table('therapy_exercise_pose_category')


    models = {
        'therapy.exercise': {
            'Meta': {'object_name': 'Exercise'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'joint_action': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'exercises'", 'symmetrical': 'False', 'to': "orm['therapy.JointAction']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pose_category': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'exercises'", 'symmetrical': 'False', 'to': "orm['therapy.PoseCategory']"}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'technique': ('django.db.models.fields.TextField', [], {})
        },
        'therapy.jointaction': {
            'Meta': {'object_name': 'JointAction'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'joint': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'muscle': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'jointActions'", 'symmetrical': 'False', 'to': "orm['therapy.Muscle']"})
        },
        'therapy.muscle': {
            'Meta': {'object_name': 'Muscle'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'muscle': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'therapy.posecategory': {
            'Meta': {'object_name': 'PoseCategory'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['therapy']