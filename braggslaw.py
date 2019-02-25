import numpy as np
import matplotlib.pyplot as plt
d=2.014
def braggs_law(theta,d):
	wavelength=(2*d*np.sin(theta))
	print(wavelength, "in Angstroms")


	voltage=(12400)/wavelength
	print(voltage,"Voltage")
	print(1/voltage, "1/Voltage")
	plt.plot(1/voltage,wavelength,'--bo')
braggs_law(9,2.014)
braggs_law(12,d)
braggs_law(15,d)
plt.show()

