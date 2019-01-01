# z1 = 1.0*exp(30(deg)j)
# z2 = 2.0*exp(60(deg)j)
# plot for z1 + z2
# z_sum = z1 + z2 = 1.86602540378+2.23205080757j
#   abs(z_sum) = 2.9093129111764098
# phase(z_sum) = 0.874478186470556

from matplotlib.pyplot import figure, show
from math import pi

fig = figure()

ax = fig.add_subplot(111, polar = True)

theta = 0.874478186470556

r = 2.9093129111764098
ax.bar(theta, r, width = 0.01)

show()
