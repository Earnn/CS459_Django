from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.sessions.models import Session
# Create your views here.
def home(request):
	request.session['x'] = request.session.get('x',0) + 1
	request.session['y'] = request.session.get('y',0) + 1
	if request.session['x']==1:
		exp = timezone.localtime(timezone.now())  +timedelta(seconds=10)
		request.session.set_expiry( 10 )
	message="x: %s, y: %s"%( request.session['x'], request.session['y'] )
	return render(request, 'home.html',
		{
			'message': message, 
			'server_datetime_local': timezone.localtime( timezone.now() ).isoformat(),
			'expiry_datetime_local': timezone.localtime( request.session.get_expiry_date() ).isoformat(),
			'expiry_datetime_utc': request.session.get_expiry_date().isoformat(),
			'session_list': Session.objects.all(),			
		})

def reset(request):
	request.session.flush()
	return redirect('home')

def resetx(request):
	try:
		del request.session['x']
	except KeyError:
		pass
	return redirect('home')



