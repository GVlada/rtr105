from numpy import *
from matplotlib import pyplot as plt

x = linspace(0, 7, 70)
y1 = cos(x)
y2 = sin(x)

plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Function $cos(x)$ and $sin(x)$')
plt.plot(x,y1, color = "#ff0000")
plt.plot(x,y2, color = "#00ff00")
plt.show()
