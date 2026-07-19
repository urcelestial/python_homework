import csv

with open("csv/employees.csv", "r") as file:
    csv_reader = csv.reader(file)
    employee_data = list(csv_reader)

full_name_list = [f"{row[1]} {row[2]}" for row in employee_data[1:]]
print("\n",full_name_list, "\n")

only_e_names = [name for name in full_name_list if "e" in name.lower()]
print(only_e_names, "\n")