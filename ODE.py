import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return (1+y**2)/(x*y)

x0=1
y0=1
a=4

def euler(f, x0, y0, a, h):
    xvalues = np.arange(x0, a+h, h)
    yvalues = [y0]

    for x in xvalues[1:]:
        y0 = y0+h*f(x0, y0)
        yvalues.append(y0)
    return xvalues, yvalues

def rk4(f, x0, y0, a, h):
    xvalues = np.arange(x0, a+h, h)
    yvalues = [y0]

    for x in xvalues[1:]:
        k1 = h*f(x0, y0)
        k2 = h*f(x0+h/2, y0+k1/2)
        k3 = h*f(x0+h/2, y0+k2/2)
        k4 = h*f(x0+h, y0+k3)
        y0 = y0+(k1+2*k2+2*k3+k4)/6
        yvalues.append(y0)
    return xvalues, yvalues

h=0.1

euler_x, euler_y = euler(f, x0, y0, a, h)
rk4_x, rk4_y = rk4(f, x0, y0, a, h)

plt.figure(figsize=(10, 6))
plt.plot(euler_x, euler_y, label='euler')
plt.plot(rk4_x, rk4_y, label='runge-kutta 4th order')
plt.grid(True, color='lightgray')
plt.legend()
plt.show()