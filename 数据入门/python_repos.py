import requests
import pygal
from pygal.style import LightColorizedStyle as LCS ,LightenStyle as LS
#执行API并储存相应
url='https://api.github.com/search/repositories?q=language:python&sort=stars'
r=requests.get(url)
print("status code："+str(r.status_code))

#把内容存储在一个变量中
response_dict=r.json()

#关于仓库的信息
repo_dicts=response_dict['items']

names,stars=[],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])#stargazers_count

#可视化
my_style=LS('#336699',base_style=LCS)
my_config=pygal.Config()
my_config.x_labels_rotation=45
my_config.show_legend=False
my_config.label_font_size=14
my_config.title_font_size=24
my_config.major_label_font_size=18
my_config.show_y_guides=False
my_config.width=1000
chart=pygal.Bar(my_config,style=my_style)#Bar中设置了类型，把x轴旋转45度，隐藏了图例
chart.title='Most-Starred Python Projects on GitHub'

chart.x_labels=names#x轴的标签是names这个列表
chart.add('',stars)
chart.render_to_file('python_repos.svg')