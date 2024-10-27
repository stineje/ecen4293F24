import numpy as np

T = np.array([300., 400., 500.])
rho = np.array([0.616, 0.525, 0.457])
coef = np.polyfit(T, rho, 2)
print("Polynomial coefficients:", coef)
# Calculate density at T = 350
dens = np.polyval(coef, 350.)
print("The density of air (kg/m^3) at 350 degC is {:.5g}".format(dens))
