import csv

# Important Items
input_file_1 = 'Batting.csv'
input_file_2 = 'People.csv'
output_file = 'batting_avg.csv'
column1 = 'AB'
column2 = 'H'
year_column = 'yearID'
check_column = 'AB'
associated_column = 'playerID'
average_column = 'average'
name_key_column = 'playerID'
name_column = 'nameFirst'
name_column_2 = 'nameLast'
threshold_year = 1939
minimum_AB = 100
minimum_to_display = 10

try:
    names_dict = {}
    # Batting read as ISO-8859-1
    with open(input_file_2, mode='r', newline='', encoding='ISO-8859-1') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            names_dict[row[name_key_column]] = row[name_column] + \
                " " + row[name_column_2]

    # People read as ISO-8859-1
    with open(input_file_1, mode='r', newline='', encoding='ISO-8859-1') as csvfile:
        reader = csv.DictReader(csvfile)
        # Add the new average and name columns
        fieldnames = reader.fieldnames + \
            [average_column, name_column, name_column_2]

        # Create a list to hold the updated rows and averages
        updated_rows = []
        valid_averages = []

        for row in reader:
            try:
                if int(row[year_column]) > threshold_year:
                    # Extract values and convert them to floats
                    value1 = float(row[column1]) if row[column1] else 0.0
                    value2 = float(row[column2]) if row[column2] else 0.0

                    # Compute the average, avoiding division by zero
                    if value1 == 0 or value2 == 0:
                        average_value = 0.0
                    else:
                        average_value = (value2 / value1)

                    row[average_column] = average_value
                    # Look up the associated name from the second CSV
                    name = names_dict.get(row[associated_column], 'Unknown')
                    row[name_column] = name

                    if float(row[check_column]) > minimum_AB:
                        valid_averages.append(
                            (average_value, row[associated_column], name))

            except ValueError:
                # Handle cases where the values are not numbers
                row[average_column] = 'N/A'
            updated_rows.append(row)

    # Write the updated rows to the output file
    with open(output_file, mode='w', newline='', encoding='ISO-8859-1') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_rows)

    # Sort and find the top averages
    valid_averages.sort(reverse=True, key=lambda x: x[0])
    top_averages = valid_averages[:minimum_to_display]

    # Output the maximum average and associated column value
    if valid_averages:
        max_average, associated_value, name = valid_averages[0]
        print(
            f"The maximum average where {check_column} is greater than {minimum_to_display} and year > {threshold_year} is: {max_average}, associated with {associated_column}: {associated_value}, name: {name}")
        print("Top 10 averages:")
        for i, (avg, assoc_val, name) in enumerate(top_averages, start=1):
            print(
                f"{i}: {avg}, associated with {associated_column}: {assoc_val}, name: {name}")
    else:
        print(
            f"No rows with {check_column} greater than {minimum_to_display} were found where year > {threshold_year}.")

except FileNotFoundError:
    print(f"Error: One of the files was not found.")
except KeyError as e:
    print(f"Error: The column '{e}' does not exist in one of the input files.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
