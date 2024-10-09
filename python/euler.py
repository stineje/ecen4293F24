import math
import numpy as np
import matplotlib.pyplot as plt

n = 1000
for i in range(1, n):
    euler_limit = (1 + 1/i)**i

euler_sum = 0.0
for n in range(n):
    euler_sum += 1 / math.factorial(n)

print(f"The Euler number is {euler_limit}")
print(f"The Euler number is {euler_sum}")
