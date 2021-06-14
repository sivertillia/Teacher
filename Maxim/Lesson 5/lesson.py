from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
import json

filename = 'data/30_days_p.json'
with open(filename) as f:
    all_data = json.load(f)

mags, lons, lats, title_text = [], [], [], []

features_all_data = all_data['features']
for i in features_all_data:
    lon = i['geometry']['coordinates'][0] # долгота
    lat = i['geometry']['coordinates'][1] # широта
    mag = i['properties']['mag']
    h_text = i['properties']['title']
    lons.append(lon)
    lats.append(lat)
    mags.append(mag)
    title_text.append(h_text)

t = title_text + mags



# data = [Scattergeo(lon=lons, lat=lats, )]
data = [{
    'type':'scattergeo',
    
    # 'locations': ['Ukraine'],
    # 'locationmode': 'country names',
    'text': t,
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    }
}]
my_layout = Layout(title="Earth")
fig = {'data': data, 'layout':my_layout, }
offline.plot(fig, filename='test.html')