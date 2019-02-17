import json
from country_codes import get_country_code
from pygal.maps.world import World
from pygal.style import RotateStyle,LightColorizedStyle
filename='population_data.json'

with open(filename) as f:
    pop_date=json.load(f)#load()运算是把filename数据赋值,这是json的方法
cc_pop1,cc_pop2,cc_pop3={},{},{}
cc_population={}
for pop_dict in pop_date:#将每个字典存储在pop_dict中
    if pop_dict['Year']=='2010':                            #for循环是一次操作一个值
        country_name=pop_dict['Country Name']

        population=int(float(pop_dict['Value']))

        code=get_country_code(country_name)

        if code:

            cc_population[code]=population          #字典的赋值
        else:
            print("ERROR"+":"+country_name)
for cc,pop in cc_population.items():
    if pop<100000000:
        cc_pop1[cc]=pop
    elif pop<1000000000:
        cc_pop2[cc]=pop
    else:
        cc_pop3[cc]=pop


wm_style=RotateStyle('#336699',base_style=LightColorizedStyle)
wm=World(style=wm_style)
wm.title="World Population in 2010,by Country"
wm.add('0-10m',cc_pop1)
wm.add('10m-1bn',cc_pop2)
wm.add('>1bn',cc_pop3)

wm.render_to_file('word_population.svg')