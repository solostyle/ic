from django.shortcuts import render_to_response, get_object_or_404
from therapy.models import Exercise, JointAction, PoseCategory, Muscle
from django.http import Http404

def index(request):
	latest_exercise_list = Exercise.objects.all().order_by('-pub_date')[:5]
	return render_to_response('exercises/index.html', {'latest_exercise_list': latest_exercise_list})

def detail(request, exercise_id):
	e = get_object_or_404(Exercise, pk=exercise_id)
	return render_to_response('exercises/detail.html', {'exercise': e})

def joints(request, exercise_id):
	return HttpResponse("Joints of Exercise %s." % exercise_id)

def categories(request, exercise_id):
	return HttpResponse("Pose categories of Exercise %s." % exercise_id)
