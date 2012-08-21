from django.template import Context, loader
from therapy.models import Exercise, JointAction, PoseCategory, Muscle
from django.http import HttpResponse

def index(request):
	latest_exercise_list = Exercise.objects.all().order_by('-pub_date')[:5]
	t = loader.get_template('exercises/index.html')
	c = Context({
		'latest_exercise_list': latest_exercise_list,
	})
	return HttpResponse(t.render(c))

def detail(request, exercise_id):
	return HttpResponse("Exercise %s." % exercise_id)

def joints(request, exercise_id):
	return HttpResponse("Joints of Exercise %s." % exercise_id)

def categories(request, exercise_id):
	return HttpResponse("Pose categories of Exercise %s." % exercise_id)
