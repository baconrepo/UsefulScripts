import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
d=2.014
n=1




V=[]
def braggs_law(theta):
	wavelength=(2*d*np.sin(theta))
	print(wavelength, "in Angstroms")

	


	voltage=(12400)/wavelength
	V=1/voltage
	#print(voltage,"Voltage")
	print(1/voltage, "1/Voltage")
	plt.plot(1/voltage,wavelength,'--bo',label='data')
	plt.ylabel("Wavelength")
	plt.xlabel("1/Voltage")
	
	varry=np.asarray(V)
	wavarry=np.asarray(wavelength)
	##curve fit##
	def yf(x,a):
		return a*x 
	#popt,pcov=curve_fit(yf,varry,wavarry)
#	print(popt)
	#plt.plot(varry,yf(varry,*popt),'r-',label='fit')



#minimum angle from bremmstrahlung in LiF
braggs_law(4)
braggs_law(5.5)
braggs_law(7)
braggs_law(9)
braggs_law(9)
braggs_law(12)
braggs_law(15)
braggs_law(19)
braggs_law(22)
plt.show()


#calculate theta from lambda
"""
wave1=1.54
pi=np.pi
theta=np.arcsin((wave1*n)/(2*d))
print(theta*180/pi)
"""
