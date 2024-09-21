import csv
import numpy as np
from scipy import stats
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Important Items
input_file = 'Batting.csv'
output_file = 'batting_avg.csv'
column_to_update = 'average_column'
year_column = 'yearID'
column1 = 'H'
column2 = 'AB'
new_name_column_display = 'avg'
associated_column = 'playerID'
threshold_year = 1950
minimum_AB = 100
minimum_to_display = 10

try:
    # Batting read as UTF-8
    with open(input_file, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames + [new_name_column_display]

        # Create a list to hold the updated rows
        updated_rows = []
        valid_averages = []

        for row in reader:
            try:
                # Extract values and convert them to floats
                value1 = float(row[column1]) if row[column1] else 0.0
                value2 = float(row[column2]) if row[column2] else 0.0

                # Compute the average, avoiding division by zero
                if value1 == 0 and value2 == 0:
                    average_value = 0.0
                else:
                    average_value = (value1 / value2)

                row[new_name_column_display] = average_value

                if float(row[column1]) >= minimum_AB:
                    valid_averages.append(
                        (average_value, row[associated_column]))

            except ValueError:
                # Handle cases where the values are not numbers
                row[new_name_column_display] = 'N/A'
            updated_rows.append(row)

    with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_rows)

    print(f"Updated file with averages saved as {output_file}")
    # Sort and find the top 10 averages
    valid_averages.sort(reverse=True, key=lambda x: x[0])
    top_averages = valid_averages[:minimum_to_display]

    # Output the maximum average and associated column value
    if valid_averages:
        max_average, associated_value = valid_averages[0]
        print(
            f"The maximum average where {column1} is >= than {minimum_AB} is: {max_average}, associated with {associated_column}: {associated_value}")
        print(f"Top {minimum_to_display} averages per season:")
        for i, (avg, assoc_val) in enumerate(top_averages, start=1):
            print(
                f"{i}: {avg:.12f}, associated with {associated_column}: {assoc_val}")
    else:
        print(f"No rows with {check_column} greater than 10 were found.")

except FileNotFoundError:
    print(f"Error: The file {input_file} was not found.")
except KeyError as e:
    print(f"Error: The column '{e}' does not exist in the input file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
