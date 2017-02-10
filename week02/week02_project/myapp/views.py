from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from forms import PersonForm
from models import Person, Image
from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore
from django.shortcuts import render


def home(request):
	return render(request, 'home.html', {'key': "value" })

def CarGallery(request):
	image_list = Image.objects.all()

	# session_list = Session.objects.all()

	# request.session['x'] = request.session.get('x',0) + 1
	# request.session['y'] = request.session.get('y',0) + 1
	# if request.session['x']==1:
	# 	exp = timezone.localtime(timezone.now())  +timedelta(seconds=10)
	# 	request.session.set_expiry( 60 )
	# message="x: %s, y: %s"%( request.session['x'], request.session['y'] )
	return render(request, 'car_gallery.html', {
			'image_list': image_list,
			
		
			 })

	# listImg =[]
def showImage(request,num="1"):
	number = num
	imageShow = Image.objects.get(id=number)

	listImg = request.session.get('key',[])
	if number in listImg:
		pass
	else:
		listImg.append(number)
	
	request.session['key'] = listImg
	if len(listImg)==1:
		request.session.set_expiry( 5 )

	preImage= [] 
	if len(preImage) <=5:
		for i in listImg:
			preImage.append(Image.objects.get(id=i))

	
		# print preImage.image.url
	# for i in Session.objects.all():
		# print SessionStore().decode(i.session_data)
		# print i
    	# print SessionStore().decode(i.session_data)

	return render(request, 'image.html', {
		'imageShow': Image.objects.get(id=num),
		'number': number,
		'listImg':listImg,
		'preImage':preImage,
			 })


	# success_url = '/'
	# return render(request, 'car_gallery.html', {'key': "value" })
# def KeepTrack(request):
# 	request.session['x'] = request.session.get('x',0) + 1
# 	request.session['y'] = request.session.get('y',0) + 1
# 	if request.session['x']==1:
# 		exp = timezone.localtime(timezone.now())  +timedelta(seconds=10)
# 		request.session.set_expiry( 10 )
# 	message="x: %s, y: %s"%( request.session['x'], request.session['y'] )
# 	return render(request, 'car_gallery.html',
# 		{
# 			'message': message, 
# 			'server_datetime_local': timezone.localtime( timezone.now() ).isoformat(),
# 			'expiry_datetime_local': timezone.localtime( request.session.get_expiry_date() ).isoformat(),
# 			'expiry_datetime_utc': request.session.get_expiry_date().isoformat(),
# 			'session_list': Session.objects.all(),			
# 		})
# def resetx(request):
# 	try:
# 		del request.session['x']
# 	except KeyError:
# 		pass
# 	return redirect('KeepTrack')

class CreatePersonView(CreateView):
	queryset = Person()
	template_name='person.html'
	form_class = PersonForm
	success_url = '/'

class UpdatePersonView(UpdateView):
	queryset = Person.objects.all()
	template_name='person.html'
	form_class = PersonForm
	success_url = '/'

class ListPersonView(ListView):
    model = Person
    template_name='person_list.html'