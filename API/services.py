import requests, json

def getPokemon(name): 
	r = requests.get('http://pokeapi.co/api/v2/pokemon/' + name.lower() + '/')
	data = r.json()
	if len(data) == 1: 
		return None
	else: 
		img_link = 'https://img.pokemondb.net/artwork/' + data['name'] + '.jpg'
		data['image'] = img_link
		gif_link = 'http://www.pokestadium.com/sprites/xy/' + data['name'] + '.gif'
		data['gif'] = gif_link
		types = list()
		for t in data['types']: 
			types.append(t['type']['name'].title())
		data['t'] = types
		abilities = list()
		for a in data['abilities']: 
			abilities.append(a['ability']['name'].title())
		data['a'] = abilities
		return data
