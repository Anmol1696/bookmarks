from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User

def main_page(request):
	template = get_template('main_page.html')
	variables = Context({
		'head_title':'Bookmarks',
		'page_title':'Welcom to Bookmarks',
		'page_body':'Here you can share and store Bookmarks'
		})
	output = template.render(variables)
	return HttpResponse(output)

def user_page(request,username):
	try:
		user = User.objects.get(username=username)
	except:
		raise Http404('Requested user no found.')
	bookmarks = user.bookmark_set.all()
	
	template = get_template('user_page.html')
	variables = Context({
		'username' : username,
		'bookmarks' : bookmarks
		})
	output = template.render(variables)
	return HttpResponse(output)