from numpy import *
import matplotlib.pyplot as plt

x = arange(0., 10, 0.3)
a = sin(x)
b = cos(x)
c = exp(x/10); d = exp(-x/10)
plt.plot(x, a, 'b-', label='sine')
plt.plot(x, b, 'r--', label='cosine')
plt.plot(x, c, 'c-.', label='exp(+x)')
plt.plot(x, d, 'gx-', linewidth=1.5, label='exp(-x)')
plt.legend(loc='upper le]')
plt.grid()
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.pause(1)
plt.show()
