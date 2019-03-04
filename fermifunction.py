import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import k
U=.2

def function(T, E):
	y=1/(np.exp((E-U)/k*T)+1)
	plt.plot(E,y,'--ro')

def frange(start, stop, step):
	i= start
	while i<stop:
		yield i
		i+=step

for i in frange(0,0.5,.1):
	function(200,i)
	function(300,i)
	function(400,i)
xx=1/(np.exp((.25-U)/(k*200)+1))
S=np.linspace(0,.5,.1)
plt.plot(S,xx)

plt.show()

