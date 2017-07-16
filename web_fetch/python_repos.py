import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=false'
# 请求数据 不是异步
r = requests.get(url)
print('Status Code:' + str(r.status_code))

response_dict = r.json()

# 'incomplete_results', 'total_count', 'items'
print('Total repositories:', response_dict['total_count'])

repo_dicts = response_dict['items']
print('Repositories returned:', len(repo_dicts))

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': str(repo_dict['description']),
        'xlink': str(repo_dict['html_url']),
    }
    plot_dicts.append(plot_dict)

# settings
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.marjor_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = True
my_config.width = 1000
my_style = LS('#333366', base_style=LCS)

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
