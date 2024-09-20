import csv
import statistics


def summarize_by_key(file_path, key_column, value_column):
    data = []

    # Read the CSV file
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)

        # Group data by the given key
        for row in reader:
            data.append(row)

    # Extract unique keys
    unique_keys = set(row[key_column] for row in data)

    # Initialize a dictionary to hold the summary results
    summary = {}

    # Summarize data for each key
    for key in unique_keys:
        # Filter rows for the current key
        filtered_rows = [float(row[value_column])
                         for row in data if row[key_column] == key]

        # Calculate summary statistics
        total = sum(filtered_rows)
        average = statistics.mean(filtered_rows)
        count = len(filtered_rows)

        # Store the results
        summary[key] = {
            'Total': total,
            'Average': average,
            'Count': count
        }

    return summary


# Usage example
file_path = 'sample.csv'
key_column = 'Year'
value_column = 'Salary'

summary = summarize_by_key(file_path, key_column, value_column)

# Output the summary with formatted values
for key, stats in summary.items():
    total_formatted = f"${stats['Total']:,.2f}"
    average_formatted = f"${stats['Average']:,.2f}"
    count_formatted = f"{stats['Count']:,}"

    print(f"{key}: Total = {total_formatted}, Average = {
          average_formatted}, Count = {count_formatted}")
