import csv

with open("../csv/employees.csv", "r") as file:
    csv_reader = csv.reader(file)

    header = next(csv_reader)

    employee_data = [row for row in csv_reader]

full_name_list = [f"{row[0]} {row[1]}" for row in employee_data]
print("\n",full_name_list, "\n")

only_e_names = [name for name in full_name_list if "e" in name.lower()]
print(only_e_names, "\n")