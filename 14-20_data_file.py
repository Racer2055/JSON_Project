import json

in_file = open("US_fires_9_14.json", 'r')

out_file = open('readable_eq_data1.json','w')

eq_data = json.load(in_file)

json.dump(eq_data,out_file, indent = 4)


list_of_eqs = eq_data


mags,lons,lats = [],[],[]

for eq in list_of_eqs:
    if(eq["brightness"] > 450):
        mags.append(eq["brightness"])
        lons.append(eq["longitude"])
        lats.append(eq["latitude"])

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [.03*mag for mag in mags],
        'color': mags,
        "colorscale": 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'}
    },
}]

my_layout = Layout(title = "US Fires - 9/1/2020 through 9/13/2020")

fig = {'data':data, 'layout':my_layout}

offline.plot(fig, filename = '09_1_2020_fires.html')
