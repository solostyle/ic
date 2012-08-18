# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Exercise'
        db.create_table('therapy_exercise', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('technique', self.gf('django.db.models.fields.TextField')()),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('therapy', ['Exercise'])

        # Adding M2M table for field joint_action on 'Exercise'
        db.create_table('therapy_exercise_joint_action', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('exercise', models.ForeignKey(orm['therapy.exercise'], null=False)),
            ('jointaction', models.ForeignKey(orm['therapy.jointaction'], null=False))
        ))
        db.create_unique('therapy_exercise_joint_action', ['exercise_id', 'jointaction_id'])

        # Adding model 'JointAction'
        db.create_table('therapy_jointaction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('joint', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('therapy', ['JointAction'])

        # Adding M2M table for field muscle on 'JointAction'
        db.create_table('therapy_jointaction_muscle', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('jointaction', models.ForeignKey(orm['therapy.jointaction'], null=False)),
            ('muscle', models.ForeignKey(orm['therapy.muscle'], null=False))
        ))
        db.create_unique('therapy_jointaction_muscle', ['jointaction_id', 'muscle_id'])

        # Adding model 'Muscle'
        db.create_table('therapy_muscle', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('muscle', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('therapy', ['Muscle'])


    def backwards(self, orm):
        # Deleting model 'Exercise'
        db.delete_table('therapy_exercise')

        # Removing M2M table for field joint_action on 'Exercise'
        db.delete_table('therapy_exercise_joint_action')

        # Deleting model 'JointAction'
        db.delete_table('therapy_jointaction')

        # Removing M2M table for field muscle on 'JointAction'
        db.delete_table('therapy_jointaction_muscle')

        # Deleting model 'Muscle'
        db.delete_table('therapy_muscle')


    models = {
        'therapy.exercise': {
            'Meta': {'object_name': 'Exercise'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'joint_action': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'exercises'", 'symmetrical': 'False', 'to': "orm['therapy.JointAction']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
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
        }
    }

    complete_apps = ['therapy']