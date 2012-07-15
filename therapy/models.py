import datetime
from django.utils import timezone
from django.db import models

class Exercise(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	joint_action = models.ManyToManyField('JointAction', related_name='exercises')
	def __unicode__(self):
		return self.name + " " + self.description
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)	
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

class JointAction(models.Model):
	joint = models.CharField(max_length=100)
	action = models.CharField(max_length=100)
	muscle = models.ManyToManyField('Muscle', related_name='jointActions')
	def __unicode__(self):
		return self.joint + " " + self.action

class Muscle(models.Model):
	muscle = models.CharField(max_length=100)
	def __unicode__(self):
		return self.muscle

# Create your models here.
