import math
import csv
import numpy as np

true = np.cos(np.pi/3)
terms = np.array([np.cos(np.pi/4), np.cos(np.pi/4)
                  - np.sin(np.pi/4)*1/math.factorial(1)*np.pi/12,
                 np.cos(np.pi/4)
                 - np.sin(np.pi/4)*1/math.factorial(1)*np.pi/12
                 - np.cos(np.pi/4)*1/math.factorial(2)*(np.pi/12)**2,
                 np.cos(np.pi/4)
                 - np.sin(np.pi/4)*1/math.factorial(1)*np.pi/12
                 - np.cos(np.pi/4)*1/math.factorial(2)*(np.pi/12)**2
                 + np.sin(np.pi/4)*1/math.factorial(3)*(np.pi/12)**3,
                 np.cos(np.pi/4)-np.sin(np.pi/4)*1/math.factorial(1)*np.pi/12
                 - np.cos(np.pi/4)*1/math.factorial(2)*(np.pi/12)**2
                 + np.sin(np.pi/4)*1/math.factorial(3)*(np.pi/12)**3
                 + np.cos(np.pi/4)*1/math.factorial(4)*(np.pi/12)**4,
                 np.cos(np.pi/4)-np.sin(np.pi/4)*1/math.factorial(1)*np.pi/12
                 - np.cos(np.pi/4)*1/math.factorial(2)*(np.pi/12)**2
                 + np.sin(np.pi/4)*1/math.factorial(3)*(np.pi/12)**3
                 + np.cos(np.pi/4)*1/math.factorial(4)*(np.pi/12)**4
                 - np.sin(np.pi/4)*1/math.factorial(5)*(np.pi/12)**5,
                 np.cos(np.pi/4)-np.sin(np.pi/4)*1/math.factorial(1)*np.pi/12
                 - np.cos(np.pi/4)*1/math.factorial(2)*(np.pi/12)**2
                 + np.sin(np.pi/4)*1/math.factorial(3)*(np.pi/12)**3
                 + np.cos(np.pi/4)*1/math.factorial(4)*(np.pi/12)**4
                 - np.sin(np.pi/4)*1/math.factorial(5)*(np.pi/12)**5
                 - np.sin(np.pi/4)*1/math.factorial(6)*(np.pi/12)**6])

abs_error = abs(terms - true)
abs_error_percent = abs((terms-true)/true)*100
array_of_values = list(zip(terms, abs_error, abs_error_percent))
for approx, abs_error, percent_abs_error in array_of_values:
    print(approx, abs_error, percent_abs_error)

# Write the data to a CSV file
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(["x", "approximation", "absolute error"])
    # Write each row to the CSV file
    for row in array_of_values:
        writer.writerow(row)


