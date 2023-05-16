import tkinter as tkt
import math
import matplotlib.pyplot as plt
import numpy as np
PI = math.pi
pi = float(180/PI)

def triangletool():
    rkfh = float(input("가로길이 = "))
    tpfh = float(input("세로길이 = "))
    dho = math.atan2(tpfh,rkfh)
    a = (rkfh**2)+(tpfh**2)
    float(a)
    eorkrtjs = math.sqrt(a)
    dhodksskdhk = dho*(180/PI)
    
    b = math.tan(math.pi * (dhodksskdhk / 180))
    print("아크탄젠트",dho)
    print("탄젠트값 = ",b)
    print("회전각 = ",dhodksskdhk)
    print("대각선 길이 = ",eorkrtjs)
    plt.axis([0,rkfh,0,tpfh])
    x = np.arange(0,100,0.1)
    y = [(b*num) for num in x]
    plt.grid()
    plt.plot(x,y)
    plt.text(0,1,"21003 kimkitae")
    plt.xlabel('가로')
    plt.ylabel('세로')
    plt.show()

triangletool()