import csv
import numpy as np
from scipy import stats
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


def linear_model(x, m, c):
    return m * x + c


def exponential_model(x, a, b):
    return a * np.exp(b * x)


def saturation_growth_rate(x, a, b):
    return (a * x) / (b + x)


def read_csv_data(file_path):
    data = []

    try:
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file)

            next(csv_reader)  # Skip the header

            for row in csv_reader:
                yearID = int(row[0])
                teamID = row[1]
                lgID = row[2]
                playerID = row[3]
                salary = float(row[4])

                data.append({
                    'Year': yearID,
                    'Team ID': teamID,
                    'League': lgID,
                    'Player ID': playerID,
                    'Salary [$]': salary
                })

        return data

    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def S(a):
    abar = np.mean(a)
    adev = a - abar
    return np.sum(adev**2)


# Usage example
data = read_csv_data('Salaries.csv')

if data:
    # Convert lists to numpy arrays for numerical operations
    salary = np.array([entry['Salary [$]']
                      for entry in data], dtype=np.float64)
    yearID = np.array([entry['Year'] for entry in data], dtype=np.float64)

    mlbbar = np.mean(salary)
    print('mean estimate = ${:,.2f}'.format(mlbbar))
    mlbmed = np.median(salary)
    print('sample median = ${:,.2f}'.format(mlbmed))

    mlbmode = stats.mode(salary, axis=None, keepdims=True)
    print(f'sample mode = ${mlbmode.mode[0]:,.2f} (count: {mlbmode.count[0]})')

    mlbvar = np.var(salary, ddof=1)
    print('sample variance = ${:,.2f}'.format(mlbvar))
    mlbstd = np.std(salary, ddof=1)
    print('sample standard deviation = ${:,.2f}'.format(mlbstd))
    mlbcv = mlbstd/mlbbar
    print('coefficient of variation = {0:5.3f} %'.format(mlbcv*100))
    Smlb = S(salary)
    print('total corrected sum of squares = ${:,.2f}'.format(Smlb))

    MADmlb = stats.median_abs_deviation(salary)
    print(f'MAD = {MADmlb/0.6745:5.3e}\n')

    # Perform exponential regression
    p_opt, p_cov = curve_fit(exponential_model, yearID, salary)

    a_fit, b_fit = p_opt
    y_fit = exponential_model(np.array(yearID), a_fit, b_fit)

    # Calculate R-squared
    ss_res = np.sum((salary - y_fit) ** 2)
    ss_tot = np.sum((salary - np.mean(salary)) ** 2)
    r_squared = 1 - (ss_res / ss_tot)

    print(f"Fitted parameters: a = {a_fit:.4f}, b = {b_fit:.4f}")
    print(f"R-squared: {r_squared:.6f}")

else:
    print("No data to process.")
