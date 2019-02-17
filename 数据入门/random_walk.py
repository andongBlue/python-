from random import choice

class RandomWalk():
    def __init__(self,num_points=5000):
        self.num_points=num_points

        #设置随机漫步的起点
        self.x_values=[0]
        self.y_values=[0]

    #随机漫步的方法
    def fill_walk(self):

        #设置漫步的截止条件：达到指定的长度
        while len(self.x_values)<self.num_points:
            x_direction = choice ([-1, 1])
            x_distance = choice ([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction=choice([-1,1])
            y_distance=choice([0,1,2,3,4])
            y_step=y_direction*y_distance

            #拒绝原地踏步
            if x_step==0 or y_step==0:
                continue#continue是跳出当前循环，在for个while中使用
           # print("y_step的值：",y_step)
            print("x_step的值：",x_step)

            next_x=self.x_values[-1]+x_step
            next_y=self.y_values[-1]+y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)