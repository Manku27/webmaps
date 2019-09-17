import folium
import pandas

def mycolor(x):
	if x < 1000:
		return 'green'
	elif 1000<=x <3000:
		return 'orange'
	else:
		return 'red'

data = pandas.read_csv("Volcanoes_USA.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map = folium.Map(location = [38.58, -99.09], zoom_start = 6, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes_USA")
fgp = folium.FeatureGroup(name= "Population")

for lt,ln,el in zip(lat,lon,elev):
	fgv.add_child(folium.CircleMarker(location=[lt,ln], popup=str(el)+"m", radius = 6, fill_color = mycolor(el), color='grey', fill_opacity = 0.7))

fgp.add_child(folium.GeoJson(data=(open('world.json','r', encoding = 'utf-8-sig').read()),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")
