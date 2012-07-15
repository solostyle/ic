from django.contrib import admin
from therapy.models import Exercise, JointAction, Muscle

class ExerciseAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['name', 'description', 'joint_action']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]

admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(JointAction)
admin.site.register(Muscle)
