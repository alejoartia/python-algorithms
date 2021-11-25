"""This is an example about how to handle json get request and how to get the response """
import requests

url_pailongas = "http://all_osrm_col_foot.smartquick.com.co/route/v1/driving/-72.51495,7.814362;-72.517893,7.814983;-72.515853,7.814194;-72.516977,7.812612;-72.510467,7.82631;-72.516827,7.815685;-72.512085,7.8162;-72.513006,7.818443;-72.510927,7.828027;-72.519179,7.802286;-72.519713,7.803107;-72.518753,7.795332;-72.509125,7.82034?overview=full&geometries=geojson&continue_straight=false"
url = "http://all_osrm_col_foot.smartquick.com.co/table/v1/driving/-72.51495,7.814362;-72.517893,7.814983;-72.515853,7.814194;-72.516977,7.812612;-72.51041,7.826293;-72.516827,7.815685;-72.512085,7.8162;-72.513006,7.818443;-72.510927,7.828027;-72.519179,7.802286;-72.519713,7.803107;-72.518753,7.795332;-72.509125,7.82034?sources=0"
r = requests.get(url)
res = r.json()
print(res)

r1 = requests.get(url_pailongas)
res2 = r1.json()
print('pailongas',res2)


#NoRoute
respuesta_error = res2['code']
print(respuesta_error)


"""list of the eliminated elements """
none_index = [i for i in range(len(res['durations'][0])) if res['durations'][0][i] is None]
print('none_index', none_index)

dictionary_destinations = {key: value for (key, value) in res.items() if key == 'destinations'}
print('dictionary_destinations', dictionary_destinations)

elementos_locations = []
for i in range(len(dictionary_destinations['destinations'])):
    dictionary_list = dictionary_destinations['destinations'][i]
    dictionary_list_a = {key: value for (key, value) in dictionary_list.items() if key == 'location'}
    elementos_locations.append(list(dictionary_list_a.values()))
    print('dictionary_list_a', dictionary_list_a)
print(elementos_locations)

"""elementos sin [[]]"""
elementos_locations_ref = [elementos_locations[i][0] for i in range(len(elementos_locations))]
print('alejo_good', elementos_locations_ref)

delete_from_route = [elementos_locations_ref[i] for i in none_index]
print('delete_from_route', delete_from_route)

none_rev = sorted(none_index, reverse=True)
print(none_rev)

for i in none_rev:
    elementos_locations_ref.pop(i)

print('elementos_locations_ref', elementos_locations_ref)

eliminated_elements = [item for item in delete_from_route if item not in elementos_locations_ref]
print('eliminated_elements', eliminated_elements)

url2 = 'http://all_osrm_col_foot.smartquick.com.co/'
url2 += 'table/v1/driving/'
for i in elementos_locations_ref:
    url2 += str(i[0])
    url2 += ','
    url2 += str(i[1])
    url2 += ';'
print(url2)

