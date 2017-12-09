import folium
import pandas as pd

data=pd.read_csv('Volcanoes_USA.txt',sep=',')
lats=list(data['LAT'])
longs=list(data['LON'])
elev=list(data['ELEV'])

def decide_color(elev):
    if elev <=1000:
        return 'green'
    elif elev <=3000:
        return 'orange'
    else:
        return 'red'


map=folium.Map(location=[38.8,-99.09],zoom_start=6,tiles="Mapbox Bright")
fg_vol=folium.FeatureGroup(name='Volcano Layer')

for lt,ln,pu in zip(lats,longs,elev):
    col=decide_color(pu)
    fg_vol.add_child(folium.CircleMarker(location=[lt,ln],popup=str(pu),color=col,radius=6,fill=True))

fg_p=folium.FeatureGroup(name='Population Layer')

fg_p.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
                            style_function=lambda x:{'fillColor': 'green' if x['properties']['POP2005']< 10000000
                                                                          else 'orange' if x['properties']['POP2005']< 20000000
                                                                          else 'red' }))

map.add_child(fg_vol)
map.add_child(fg_p)
map.add_child(folium.LayerControl())

map.save('Map1.html')
