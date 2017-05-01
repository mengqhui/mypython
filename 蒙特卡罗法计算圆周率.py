#coding:utf8
#问题描述:蒙特卡罗法计算圆周率
#一个圆半径R，它有一个外切正方形边长2R。
#可以知道：
#圆面积=Pi R^2
#正方形面积 2R x 2R=4R^2
#从这个正方形内随机抽取一个点，对这个点的要求是在正方形内任意一点的概率平均分布。
#那么这个点在圆以内的概率大概就是pi*R^2/4R^2=pi/4
#生成若干个这样的点，利用平面上两点间距离公式计算这个点到圆心的距离来判断是否在圆内。
#当我们使用足够多的点来进行统计时，我们得到的概率值十分接近pi/4
#这样就可以得到pi值

import random 
import math
def main():
    print '请输入迭代的次数：'
    n=int(raw_input())   #n是随机的次数  
    total=0   #total是所有落入圆内的随机点
    for i in xrange(n):
        x=random.random()
        y=random.random()
        if math.sqrt(x**2+y**2)<1.0:   #判断是否落入圆内
            total+=1
    mypi=4.0*total/n   #得到Pi值
    print '迭代次数是',n,'Pi的值是：',mypi
    print '数学pi：',math.pi
    print '误差是：',abs(math.pi-mypi)/math.pi   #计算误差
    
main()