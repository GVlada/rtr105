Python 2.7.13 (default, Sep 26 2018, 18:42:22) 
[GCC 6.3.0 20170516] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from cmath import exp
>>> from cmath import phase
>>> from math import pi
>>> z1 = 1.0*exp(30.0*pi/180.0*1j)
>>> print(z1)
(0.866025403784+0.5j)
>>> z2 = 2.0*exp(60.0*pi/180.0*1j)
>>> print(z1)
(0.866025403784+0.5j)
>>> z_sum = z1 + z2
>>> z_sub = z1 - z2
>>> z_mul = z1 * z2
>>> z_div = z1 / z2
>>> print(z_sum)
(1.86602540378+2.23205080757j)
>>> print(z_sub)
(-0.133974596216-1.23205080757j)
>>> print(z_mul)
(4.4408920985e-16+2j)
>>> print(z_div)
(0.433012701892-0.25j)
>>> abs(z_sum)
2.9093129111764098
>>> phase(z_sum)
0.8744781864705565
>>> abs(z_sub)
1.2393136749274758
>>> phase(z_sub)
-1.6791118635716693
>>> abs(z_mul)
2.0
>>> phase(z_mul)
1.5707963267948963
>>> abs(z_div)
0.5
>>> phase(z_div)
-0.5235987755982987
>>> 
