# z1 = 1.0*exp(30(deg)j)
# z2 = 2.0*exp(60(deg)j)
# plot for z1 - z2
# z_sum = z1 - z2 = -0.133974596216-1.23205080757j
#   abs(z_sub) = 1.2393136749274758
# phase(z_sub) = -1.679111863571669

from matplotlib.pyplot import figure, show
from math import pi

fig = figure()

ax = fig.add_subplot(111, polar = True)

theta = -1.679111863571669

r = 1.2393136749274758
ax.bar(theta, r, width = 0.01)

show()
