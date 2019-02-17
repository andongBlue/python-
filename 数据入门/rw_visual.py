import matplotlib.pyplot as plt
from random_walk import RandomWalk
import warnings

warnings.filterwarnings('ignore')
while True:

    rw=RandomWalk(50000)
    rw.fill_walk()
    point_numbers=list(range(rw.num_points))

    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,s=12)#颜色映射的格式

    plt.axes().get_xaxis ().set_visible (False)
    plt.axes().get_yaxis ().set_visible (False)
    plt.scatter(0,0,c='red',edgecolors='none',s=50)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='green',edgecolors='none',s=50)

    plt.show()

    rw_active=input("输入是否继续（Y/N)?:")
    if rw_active=='n'or rw_active=='N':
        break
