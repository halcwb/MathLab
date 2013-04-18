import numpy as np
import matplotlib.pyplot as plt

def simplifyradical(n, r):
	f = max([i for i in range(1, n + 1) if n % i**r == 0])
	return (f, n / (f ** r))

def addvect(a,b):
	x1,y1 = a
	x2,y2 = b
	return (x1 + x2, y1 + y2)

def subtrvect(a,b):
	x1,y1 = a
	x2,y2 = b
	return (x1 - x2, y1 - y2)

def multvect(a, b):
	x,y = a
	return (x*b, y*b)
	
def midpoint(a,b):
	x1,y1 = a
	x2,y2 = b
	return ((x1 + x2)/2., (y1 + y2)/2.)
	
def distance(a,b):
	x1,y1 = a
	x2,y2 = b
	return np.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))	
def slope(a,b):
	x1,y1 = a
	x2,y2 = b
	return (float(y2) - y1)/(float(x2) - x1)
	
#y = map(lambda x: np.sqrt((10 - x**2)/7.), range(0,10))
#x = map(lambda x: (x**2), range(0,10))
 
print midpoint((-11.,32.),(-1.,3.))
print np.sqrt(52)

fig = plt.figure(facecolor='white')
ax = fig.add_subplot(1,1,1, aspect='equal')
ax.set_title(r'$y=3x-2$')
#ax.plot(x,y)
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.autoscale_view(tight=True)
#ax.set_ylim(min(y),max(y))
#ax.set_xlim(min(x),max(x))
#ax.set_xticks(x)
#ax.set_xticklabels(['', r'$$', r'$$'])
#ax.text(2*np.pi + .1, -.2, r'$t$') # Manually adjusted
 
#plt.savefig('plot.pdf')
#plt.show()

