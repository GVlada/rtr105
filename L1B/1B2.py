from numpy import *
from matplotlib import pyplot as plt
from math import factorial as fact

x = linspace(0, 7, 70)
f0 = sin(x)
f1 = x
f2 = f1 - x**3/fact(3)
f3 = f2 + x**5/fact(5)
f4 = f3 - x**7/fact(7)

plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Function $sin(x)$ approximation')
plt.plot(x, f0, color = "#ff0000")	# red
plt.plot(x, f1, color = "#00ff00")	# green
plt.plot(x, f2, color = "#0000ff")	# blue
plt.plot(x, f3, color = "#ff00ff")	# magenta
plt.plot(x, f4, color = "#00ffff")	# cyan
plt.show()
