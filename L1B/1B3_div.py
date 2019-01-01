# z1 = 1.0*exp(30(deg)j)
# z2 = 2.0*exp(60(deg)j)
# plot for z1 / z2
# z_div = z1 / z2 = 0.433012701892-0.25j
#   abs(z_div) = 0.5
# phase(z_div) = -0.5235987755982987

from matplotlib.pyplot import figure, show
from math import pi

fig = figure()

ax = fig.add_subplot(111, polar = True)

theta = -0.5235987755982987

r = 0.5
ax.bar(theta, r, width = 0.01)

show()
