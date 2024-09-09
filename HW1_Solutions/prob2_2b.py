import math

start = 1.0
end = 5.0
number_values = 10

# Calculate the step size
step = (end - start) / (number_values - 1)
numbers = [start + i*step
           for i in range(number_values)]

# Calculate the function
y = [(3*t-2)/4/t - math.pi/2*t for t in numbers]

# Print the results
for t_ans, y_ans in zip(numbers, y):
    print(f"y({t_ans}) = {y_ans}")
