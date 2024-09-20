import csv

with open("people.csv", mode="r", newline='') as file:
    input_file = csv.DictReader(file)

    max_age = None
    oldest_person = None
    # Convert the reader to a list to allow multiple iterations
    rows = list(input_file)

    for row in rows:
        age = int(row["age"])
        if max_age is None or max_age < age:
            max_age = age
            oldest_person = row["name"]

    for row in rows:
        print(row)

if max_age is not None:
    print(f"The oldest person is {oldest_person}, who is {max_age} years old.")
else:
    print("The file does not contain any people.")
