import numpy as np
import matplotlib.pyplot as plt

def rectanglemethod(func, a, b):
    x = np.linspace(a, b, 20)
    y = func(x)
    plt.plot(x, y, "bo-")
    
    integrale = 0
    for i in range(19):
        integrale = integrale + y[i]*(x[i+1]-x[i])
        x_rect = [x[i], x[i], x[i+1], x[i+1], x[i]]
        y_rect = [0   , y[i], y[i]  , 0     , 0   ]
        plt.plot(x_rect, y_rect,"r")
    print("integrale = ", integrale)
    
    plt.show()
    
func = lambda x:np.cos(x)
xmin = 0
xmax = 3*np.pi/2
rectanglemethod(func, xmin, xmax)
