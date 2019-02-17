import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename='death_valley_2014.csv'

with open(filename) as f:#with来读写文件e
    reader=csv.reader(f)
    header_row=next(reader)
    for index,column_header in enumerate(header_row):#enumerate()方法是获得读取数据的索引和内容
       print(index,column_header)
    highs,date,lows=[],[],[]#这个写法*

    for row in reader:
        try:
            current_date=datetime.strptime(row[0],"%Y-%m-%d")#这里%y是指：两位数的年份(eg:15)；%Y是个指四位数的年份(eg:2015 )
            high=int(row[1])
            low=int(row[3])
        except ValueError:
            print(current_date,"丢失数据")
        else:
            date.append(current_date)

            highs.append(high)
            lows.append(low)
   # max_y=max(highs)
    #print(max_y)
    fig=plt.figure(dpi=128,figsize=(10,6))
    plt.plot(date,highs,c='red',alpha=0.5)
    plt.plot(date,lows,c='blue',alpha=0.5)
    plt.fill_between(date,highs,lows,facecolor='yellow',alpha=0.7)#fill_between()填充之间的颜色，（横轴，纵轴1，纵轴2....)
    #设置表格的格式
    #plt.yticks(y for y in range(max_y+1))
    #ax=plt.gca()
    #设置y轴的刻度
    #ax.locator_params("j",nbins=5)
    plt.title("Daily high and low temperature 2014",fontsize=24)
    plt.xlabel('',fontsize=16)
    plt.ylabel("Temperature(F)",fontsize=16)
    plt.tick_params(axis='x',which='major',labelsize=10)
    fig.autofmt_xdate()#当x轴太拥挤了，可以自适应

    plt.show()