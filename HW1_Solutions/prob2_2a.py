import math

start = 0.1
end = 0.25
number_values = 10

# Calculate the step size
step = (end - start) / (number_values - 1)
numbers = [start + i*step
           for i in range(number_values)]

# Calculate the function
y = [(6*t**3-3*t-4)/8/math.sin(5*t) for t in numbers]

# Print the results
for t_value, y_value in zip(numbers, y):
    print(f"y({t_value}) = {y_value}")
