from django.http import HttpResponse

def index(request):
	return HttpResponse("Therapy index.")

def detail(request, exercise_id):
	return HttpResponse("Exercise %s." % exercise_id)

def joints(request, exercise_id):
	return HttpResponse("Joints of Exercise %s." % exercise_id)

def categories(request, exercise_id):
	return HttpResponse("Pose categories of Exercise %s." % exercise_id)
