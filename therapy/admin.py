from django.contrib import admin
from therapy.models import Exercise, JointAction, Muscle

class ExerciseAdmin(admin.ModelAdmin):
	fields = ['pub_date', 'name', 'description', 'joint_action']

admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(JointAction)
admin.site.register(Muscle)
