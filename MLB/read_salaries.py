import csv
import numpy as np
from scipy import stats
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


def linear_model(x, m, c):
    return m * x + c


def read_csv_data(file_path):
    data = []

    # Open the CSV file and read its content
    try:
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file)

            # Skipping the header row
            next(csv_reader)

            # Process each row
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


# Usage example
data = read_csv_data('Salaries.csv')


def S(a):
    abar = np.mean(a)
    adev = a - abar
    return np.sum(adev**2)


# Check if data was successfully read
if data:
    salary = [entry['Salary [$]']
              for entry in data]
    playerID = [entry['Player ID']
                for entry in data]
    yearID = [entry['Year']
              for entry in data]

    mlbbar = np.mean(salary)
    print('mean estimate = ${:,.2f}'.format(mlbbar))
    mlbmed = np.median(salary)
    print('sample median = ${:,.2f}'.format(mlbmed))
    mlbmode = stats.mode(salary, axis=None)
    print('sample mode = ${:,.2f}'.format(mlbmode.mode),
          ' (count: ', mlbmode.count, ')')
    mlbvar = np.var(salary, ddof=1)
    print('sample variance = ${:,.2f}'.format(mlbvar))
    mlbstd = np.std(salary, ddof=1)
    print('sample standard deviation = ${:,.2f}'.format(mlbstd))
    mlbcv = mlbstd/mlbbar
    print('coefficient of variation = {0:5.3f} %'.format(mlbcv*100))
    Smlb = S(salary)
    print('total corrected sum of squares = ${:,.2f}'.format(Smlb))
    MADmlb = stats.median_abs_deviation(salary)
    print('MAD = {0:5.3e}'.format(MADmlb/0.6745), end='\n\n')

    # Use curve_fit to perform the least squares fit
    # p_opt contains the optimal values for the parameters (m, c)
    # p_cov is the covariance of the parameters (optional)
    p_opt, p_cov = curve_fit(linear_model, yearID, salary)

    # Extract the fitted slope and intercept
    m_fit, c_fit = p_opt

    # Calculate the fitted y-values
    y_fit = linear_model(np.array(yearID), m_fit, c_fit)

   # Compute residuals (difference between observed and fitted values)
    residuals = salary - y_fit

    # Extract the optimal parameters (slope and intercept)
    slope, intercept = p_opt

    # Compute the standard deviation of the parameters (errors on slope and intercept)
    slope_error, intercept_error = np.sqrt(np.diag(p_cov))

    # Compute the residual sum of squares (SS_res)
    ss_res = np.sum((salary - y_fit) ** 2)

    # Compute the total sum of squares (SS_tot)
    y_mean = np.mean(salary)
    ss_tot = np.sum((salary - y_mean) ** 2)

    # Compute R-squared
    r_squared = 1 - (ss_res / ss_tot)

    # Output the result
    print(f"Fitted slope: ${slope:,.2f} ± ${slope_error:,.2f}")
    print(f"Fitted intercept: ${intercept:,.4f} ± ${intercept_error:,.4f}")
    print(
        f"Residual standard deviation (error bar value): {np.std(residuals):.2f}")
    print(f"R-squared: {r_squared:.6f}")

# Plot the original data points
plt.scatter(yearID, salary, label='Data points')

# Plot the least-squares fit line
plt.plot(yearID, y_fit, color='red',
         label=f'Fit: $y = {m_fit:,.4f}x + {c_fit:,.4f}$')

# Add labels and a legend
plt.xlabel('x')
plt.ylabel('y')
plt.title('Least Squares Fit using SciPy')
plt.legend()

# Show the plot
plt.savefig('read-salaries.png')
plt.show()
