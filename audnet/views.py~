from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib.auth import logout as auth_logout
from posts.views import posts
from django.contrib import auth
from forms import MyRegistrationForm

def index(request):
	if request.user.is_authenticated():
		return posts(request)
	else:
		args = {}
		args.update(csrf(request))

		return render_to_response('index.html',args)


#Logs the user out
def logout(request):
	auth_logout(request)
	args = {}
	args.update(csrf(request))
	return index(request)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)
	
	if user is not None:
		auth.login(request, user)
		return posts(request)
	else:
		args = {}
		args.update(csrf(request))
		args['error'] = '**INVALID USERNAME OR PASSWORD**'
		return render_to_response('index.html',args)

def register(request):
	if request.method == 'POST':
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
		args = {}
		args.update(csrf(request))
		args['error'] = 'Registration Successful!'
		return render_to_response('index.html',args)


	args = {}
	args.update(csrf(request))

	args['form'] = MyRegistrationForm()

	return render_to_response('register.html', args)
	





