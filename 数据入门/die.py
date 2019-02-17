from random import randint

class Die():
    #构造方法
    def __init__(self,num_sides=6):
        self.num_sides=num_sides

    def roll(self):
        #随机返回一个(1,6)的值
        return randint(1,self.num_sides)