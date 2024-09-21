import csv

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
threshold_year = 1939
minimum_AB = 500
minimum_to_display = 10

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

    top_averages = valid_averages[:minimum_to_display]

    if valid_averages:
        max_average, associated_value, first_name, last_name = valid_averages[0]
        print(f"The maximum average where the {check_column} is greater than {minimum_AB} and year > {threshold_year} is: "
              f"{max_average}, associated with {associated_column}: {associated_value}, name: {first_name} {last_name}")
        print(f"Top {minimum_to_display} averages:")
        for i, (avg, key, first_name, last_name) in enumerate(top_averages, start=1):
            print(
                f"{i}: {avg}, associated with {associated_column}: {key}, name: {first_name} {last_name}")
    else:
        print(
            f"No rows with {check_column} greater than {minimum_AB} were found where year > {threshold_year} and total > {minimum_AB}.")

except FileNotFoundError:
    print(f"Error: One of the files was not found.")
except KeyError as e:
    print(f"Error: The column '{e}' does not exist in one of the input files.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
