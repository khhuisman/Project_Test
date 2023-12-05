print('hello world')

import numpy as np

def circumference_circle(r):
	return 2*np.pi*r

def area_circle(r):
	return np.pi*(r**2)
r0 = 2
print('The area of a circle of a circle with radius r = {} is {}'.format(r0,area_circle(r0)))
