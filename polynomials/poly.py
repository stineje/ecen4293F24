import numpy as np

a = [1, -3.5, 2.75, 2.125, -3.875, 1.25]
r = np.roots(a)
for i in r:
    # Check if there is an imaginary part
    if i.imag != 0:
        print(f"Polynomial root: {i.real:.8f} + {i.imag:.8f}j")
    else:
        print(f"Polynomial root: {i.real:.8f}")
