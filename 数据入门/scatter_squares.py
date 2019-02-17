import matplotlib.pyplot as plt

x_vaules=list(range(1,1001))
y_vaules=list(x**2 for x in x_vaules)

""""
    使用了颜色映射，数字的颜色跟着y轴的数字不断变大
    随机漫步的c=y_vaules中等号右边的是一个list，其中颜色的变化是根据list里面的内容变化的
"""
plt.scatter(x_vaules,y_vaules,c=y_vaules,cmap=plt.cm.Blues,edgecolor='none',s=100)#s是一个点的大小

#为坐标设置取值范围
plt.axis([0,1100,0,1100000])#axis的参数是x与y坐标起始点和最大值

#plt.show()

#保存这个图像，第一个参数是设置这个图像的格式，第二个参数是设置这个图像的多余的空白区域剪裁掉，这个图片保存在当前文件夹下面
plt.savefig("squares_fig.png",bbox_inches='tight')