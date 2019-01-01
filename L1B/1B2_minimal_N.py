from math import sin
from math import pi as PI

epsilon = 0.01	# desired precision

def my_sin(x, N):
	k = 0
	a = (-1)**0*x**1/(1)
	S = a
	
	while k < N:
		k = k + 1
		R = (-1)*x*x/ ( (2*k)*(2*k+1) )
		a = a * R
		S = S + a
	return S

x = PI
y1 = 0 # sin(PI) = 0

N = 0
y2 = my_sin(x, N)
while abs(y2) - y1 > epsilon:
	N = N + 1
	y2 = my_sin(x,N)

print("There is needed '%d' terms in Taylor series to reach %f precision at point %f"%(N, epsilon, x))
