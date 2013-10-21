from django.shortcuts import render_to_response, get_object_or_404

def error_404(request):

	return render_to_response('404.html')