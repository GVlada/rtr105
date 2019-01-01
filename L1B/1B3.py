from matplotlib.pyplot import figure, show
from math import pi

fig = figure()

ax = fig.add_subplot(111, polar = True)

theta = [30, 60]
theta = [i*pi/180 for i in theta]

r = [1., 2.0]
ax.bar(theta, r, width = 0.01)

show()
