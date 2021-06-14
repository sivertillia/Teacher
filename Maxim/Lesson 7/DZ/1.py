# Get this figure: fig = py.get_figure("https://plotly.com/~EndlessRain/62/")
# Get this figure's data: data = py.get_figure("https://plotly.com/~EndlessRain/62/").get_data()
# Add data to this figure: py.plot(Data([Scatter(x=[1, 2], y=[2, 3])]), filename ="male (1)", fileopt="extend")
# Get z data of first trace: z1 = py.get_figure("https://plotly.com/~EndlessRain/62/").get_data()[0]["z"]

# Get figure documentation: https://plotly.com/python/get-requests/
# Add data documentation: https://plotly.com/python/file-options/

# If you're using unicode in your file, you may need to specify the encoding.
# You can reproduce this figure in Python with the following code!

# Learn about API authentication here: https://plotly.com/python/getting-started
# Find your api_key here: https://plotly.com/settings/api

from plotly import offline
from plotly.graph_objs import *
# py.sign_in('username', 'api_key')
trace1 = {
  "uid": "47acff", 
  "type": "choropleth", 
  "zmax": 250, 
  "zmin": 1, 
  "z": ["51", "108", "219", "1328", "25", "27", "79", "3", "34", "108", "46", "57", "3", "30", "103", "103", "18", "56", "2", "17", "41", "13", "53", "2", "3", "61", "36", "25", "65", "26", "3", "12", "7", "29", "4", "2", "20", "17", "27", "7", "3", "1", "3", "4", "3", "5", "4", "11", "1", "5", "1", "2", "7", "2", "5", "2", "4", "6", "2", "1", "4", "8", "1", "2", "3", "5", "29", "1", "4", "2", "3", "1", "1", "1", "5", "1", "1", "1", "3", "1", "2", "1", "1", "1", "1", "1", "2", "1", "1", "1", "1", "1", "1", "219"], 
  "zauto": False, 
  "colorbar": {"tickfont": {"size": 16}}, 
  "colorscale": [[0, "rgb(0,0,0)"], [0.2, "rgb(230,0,0)"], [0.4, "rgb(230,210,0)"], [0.7, "rgb(255,255,255)"], [1, "rgb(160,200,255)"]],
  "locationmode": "country names", 
  "locations": ["Switzerland", "United Kingdom", "Germany", "United States", "Great Britain", "Finland", "Canada", "Qatar", "Belgium", "France", "Australia", "India", "Bangladesh", "South Korea", "Japan", "Italy", "Denmark", "Netherlands", "Ghana", "Aotearoa", "Sweden", "Singapore", "Brazil", "Russian Federation", "Haiti", "Spain", "Austria", "Ireland", "China", "Portugal", "Czech Republic", "Argentina", "Turkey", "Israel", "Cyprus", "Egypt", "Norway", "Hong Kong", "Greece", "South Africa", "Taiwan", "England", "Colombia", "Mexico", "Kenya", "Saudi Arabia", "Estonia", "Chile", "TL", "United Arab Emirates", "Namibia", "Malta", "Hungary", "Cameroon", "Benin", "Bulgaria", "Luxembourg", "Pakistan", "Indonesia", "Costa Rica", "Slovak Republic", "Malaysia", "Russia", "Romania", "Cambodia", "Hrvatska", "Northern Ireland", "Oman", "Iran", "Venezuela", "Cuba", "Greenland", "Ecuador", "Iceland", "Poland", "Ukraine", "Rwanda", "Uruguay", "Tunisia", "Libya", "Viet Nam", "Morocco", "Swaziland", "Solomon Islands", "Macau", "Guadeloupe", "Slovenia", "Zambia", "Thailand", "Philippines", "Latvia", "Chad", "Lebanon", "Germany"], 
  "autocolorscale": False
}
data = Data([trace1])
layout = {
  "geo": {
    "showframe": False, 
    "showcountries": True
  }, 
  "title": "", 
  "width": 1044, 
  "height": 507, 
  "margin": {
    "b": 10, 
    "l": 10, 
    "r": 10, 
    "t": 10
  }, 
  "autosize": True, 
  "showlegend": True
}
fig = {'data': data, 'layout':layout, }
offline.plot(fig, filename='test.html')