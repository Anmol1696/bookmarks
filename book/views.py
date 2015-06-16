from django.shortcuts import render, render_to_response

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.contrib.auth import logout
from book.forms import *


def main_page(request):
	return render_to_response('main_page.html', RequestContext(request))

def user_page(request,username):
	try:
		user = User.objects.get(username=username)
	except:
		raise Http404('Requested user no found.')
	bookmarks = user.bookmark_set.all()
	return render_to_response('user_page.html', {'username' : username,'bookmarks' : bookmarks}, context_instance = RequestContext(request))

def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/')

def register_page(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(
				username = form.cleaned_data['username'],
				password = form.cleaned_data['password1'],
				email = form .cleaned_data['email']
			)
			return HttpResponseRedirect('/register/success')
	else:
		form = RegistrationForm()
	variables = RequestContext(request,{ 'form' : form })
	return render_to_response(
		'registration/register.html',
		variables
	)