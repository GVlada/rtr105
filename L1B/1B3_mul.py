# z1 = 1.0*exp(30(deg)j)
# z2 = 2.0*exp(60(deg)j)
# plot for z1 * z2
# z_mul = z1 * z2 = 4.4408920985e-16+2j
#   abs(z_mul) = 2.0
# phase(z_mul) = 1.5707963267948963

from matplotlib.pyplot import figure, show
from math import pi

fig = figure()

ax = fig.add_subplot(111, polar = True)

theta = 1.5707963267948963

r = 2.0
ax.bar(theta, r, width = 0.01)

show()
