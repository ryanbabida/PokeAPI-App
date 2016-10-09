from django.shortcuts import render
from API.services import *

# Create your views here.
def homeView(request): 
	name = ''
	err_message = None
	data = dict()
	found = 1
	if request.POST: 
		if 'input' in request.POST and request.POST['input'] != '':
			name = request.POST['input'].rstrip()
			data = getPokemon(name)
			if data:
				data['name'] = data['name'].title()
			found = 1
		else:
			err_message = 'No Pokemon name entered. Please enter a name.'

	if data == None: 
		found = 0

	context = {
		'name': name.title(),
		'err_message': err_message,
		'data': data,
		'found': found
	}
	return render(request, 'home.html', context)
