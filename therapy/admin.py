from django.contrib import admin
from therapy.models import Exercise, JointAction, Muscle

class JointActionInline(admin.StackedInline):
	model = JointAction
	extra = 3

class ExerciseAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['name', 'description', 'technique', 'joint_action', 'pose_category']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	list_display = ('name', 'description', 'pose_category', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['name']
	date_hierarchy = 'pub_date'


admin.site.register(Exercise, ExerciseAdmin)

class MuscleInline(admin.StackedInline):
	model = Muscle
	extra = 3

class JointActionAdmin(admin.ModelAdmin):
	inlines = [MuscleInline]

admin.site.register(JointAction)
admin.site.register(Muscle)
