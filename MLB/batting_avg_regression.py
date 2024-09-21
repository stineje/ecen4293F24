import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Important Items
input_file_1 = 'Batting.csv'
input_file_2 = 'People.csv'
output_file = 'batting_avg_summary.csv'
column1 = 'AB'
column2 = 'H'
year_column = 'yearID'
total_column = 'AB'
check_column = 'AB'
associated_column = 'playerID'
average_column = 'average'
name_key_column = 'playerID'
name_column_1 = 'nameGiven'
name_column_2 = 'nameFirst'
name_column_3 = 'nameLast'
threshold_year = 1970
minimum_AB = 500
minimum_to_display = 25


def linear_model(x, m, c):
    return m * x + c


try:
    names_dict = {}
    # People read as ISO-8859-1
    with open(input_file_2, mode='r', newline='', encoding='ISO-8859-1') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            names_dict[row[name_key_column]] = {
                'first_name': row[name_column_2],
                'last_name': row[name_column_3]
            }

    summary = {}
    # Batting read as ISO-8859-1
    with open(input_file_1, mode='r', newline='', encoding='ISO-8859-1') as csvfile:
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames + \
            [average_column, name_column_2, name_column_3]

        for row in reader:
            year = int(row[year_column])
            total_value = float(
                row[total_column]) if row[total_column] else 0.0

            if year > threshold_year:
                key = row[associated_column]
                value1 = float(row[column1]) if row[column1] else 0.0
                value2 = float(row[column2]) if row[column2] else 0.0

                if key not in summary:
                    summary[key] = {'sum1': 0, 'sum2': 0,
                                    'total_sum': 0, 'count': 0}

                summary[key]['sum1'] += value1
                summary[key]['sum2'] += value2
                summary[key]['total_sum'] += total_value
                summary[key]['count'] += 1

    valid_averages = []

    for key, data in summary.items():
        total_sum1 = data['sum1']
        total_sum2 = data['sum2']
        total_sum = data['total_sum']
        count = data['count']

        # Avoid division by zero
        if total_sum1 == 0 and total_sum2 == 0:
            average_value = 0.0
        else:
            average_value = total_sum2 / total_sum1

        if total_sum > minimum_AB:
            first_name = names_dict[key]['first_name']
            last_name = names_dict[key]['last_name']
            valid_averages.append((average_value, key, first_name, last_name))

    # Sort the valid averages before writing
    valid_averages.sort(reverse=True, key=lambda x: x[0])

    # Write the results to a new CSV file
    with open(output_file, mode='w', newline='', encoding='ISO-8859-1') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=[
                                associated_column, average_column, name_column_2, name_column_3])
        writer.writeheader()

        for average_value, key, first_name, last_name in valid_averages:
            writer.writerow({
                associated_column: key,
                average_column: average_value,
                name_column_2: first_name,
                name_column_3: last_name
            })

        x_data = []
        y_data = []

        for average_value, key, first_name, last_name in valid_averages:
            x_data.append(summary[key]['total_sum'])
            y_data.append(average_value)

        # Convert lists to numpy arrays for curve_fit
        x_data = np.array(x_data)
        y_data = np.array(y_data)

        # Use curve_fit to perform the least squares fit
        if len(x_data) > 1 and len(y_data) > 1:
            p_opt, p_cov = curve_fit(linear_model, x_data, y_data)
        else:
            print("Not enough data points for curve fitting.")

        # Extract the fitted slope and intercept
        m_fit, c_fit = p_opt

        # Calculate the fitted y-values
        y_fit = linear_model(x_data, m_fit, c_fit)

        # Compute the residual sum of squares (SS_res)
        ss_res = np.sum((y_data - y_fit) ** 2)

        # Compute the total sum of squares (SS_tot)
        y_mean = np.mean(y_data)
        ss_tot = np.sum((y_data - y_mean) ** 2)

        # Compute R-squared
        r_squared = 1 - (ss_res / ss_tot)

        # Output the result
        print(f"R-squared: {r_squared:.6f}")

        # Plot the original data points
        plt.scatter(x_data, y_data, label='Data points')

        # Plot the least-squares fit line
        plt.plot(x_data, y_fit, color='red',
                 label=f'Fit: y = {m_fit:.4f}x + {c_fit:.4f}')

        # Add labels and a legend
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Least Squares Fit using SciPy')
        plt.legend()

        # Show the plot
        plt.savefig('batting_avg_regression.png')
        plt.show()

    top_averages = valid_averages[:minimum_to_display]

    if valid_averages:
        print(f"Success: found averages that fit the model.")
    else:
        print(
            f"No rows with {check_column} greater than {minimum_AB} were found where year > {threshold_year} and total > {minimum_AB}.")


except FileNotFoundError:
    print(f"Error: One of the files was not found.")
except KeyError as e:
    print(f"Error: The column '{e}' does not exist in one of the input files.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
