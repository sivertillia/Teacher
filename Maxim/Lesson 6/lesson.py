import requests

from plotly.graph_objs import Bar
from plotly import offline

url = 'https://api.github.com/search/repositories?q=sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(r.status_code)
repos = r.json()
repo_items = repos['items']
repo_links, repo_names, stars = [], [], []

for repo in repo_items:
    repo_names.append(repo['name'])
    stars.append(repo['stargazers_count'])

    repo_link = f"<a href=\"{repo['html_url']}\">{repo['name']}</a>"

    repo_links.append(repo_link)

data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'marker': {
        'color': '#ff0000',
        'line': {'width': 2.5,'color': 'rgb(25, 25, 25)'},  
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'TEst',
    'xaxis' : {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14}
    },
    'yaxis' : {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    }
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig)