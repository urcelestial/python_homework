# Task 2

import csv
from datetime import datetime
import traceback
import os
import custom_module

def read_employees():
    employees_data = {}
    rows_list = []
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        csv_path = os.path.join(current_dir, "..", "csv", "employees.csv")

        with open(csv_path, "r") as file:
            csv_reader = csv.reader(file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    employees_data["fields"] = row
                else:
                    rows_list.append(row)
                line_count += 1

        employees_data["rows"] = rows_list    
        return employees_data

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")


# Task 3
def column_index(column_name):
    idx = employees["fields"].index(column_name)
    return idx

# Task 4
def first_name(row_number):
    idx = column_index("first_name")
    return employees["rows"][row_number][idx]

# Task 5
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches = list(filter(employee_match, employees['rows']))
    return matches

# Task 6
def employee_find_2(employee_id):
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
    return matches

# Task 7 
def sort_by_last_name():
    employees["rows"].sort(key=lambda row: row[column_index("last_name")])
    return employees["rows"]

# Task 8 
def employee_dict(employee_row):
    result_dict = {}

    for i in range(len(employees["fields"])):

        # Skipping the employee_id column
        if employees["fields"][i] == "employee_id":
            continue

        header_label = employees["fields"][i]
        row_value = employee_row[i]
        result_dict[header_label] = row_value
    return result_dict

# Task 9
def all_employees_dict():
    master_dict = {}
    for row in employees["rows"]:
        employee_id = row[employee_id_column]
        new_folder = employee_dict(row)
        master_dict[employee_id] = new_folder
    return master_dict


# Task 10
def get_this_value():
    return os.getenv("THISVALUE")


# Task 11
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

# Task 12
def parse_minutes_file(relative_path):
    data_dict = {}
    rows_list = []
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, *relative_path.split("/"))

    with open(csv_path, "r") as file:
        csv_reader = csv.reader(file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                data_dict["fields"] = row
            else:
                rows_list.append(tuple(row))  # Saved as a tuple
            line_count += 1

    data_dict["rows"] = rows_list
    return data_dict

def read_minutes():
    minutes1 = parse_minutes_file("../csv/minutes1.csv")
    minutes2 = parse_minutes_file("../csv/minutes2.csv")
    return minutes1, minutes2

# Task 13
def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])

    combined_set = set1 | set2
    return combined_set

# Task 14
def create_minutes_list():
    raw_list = list(minutes_set)
    
    mapped_object = map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), raw_list)
    
    return list(mapped_object)

# Task 15
def write_sorted_list():
    sorted_raw = sorted(minutes_list, key=lambda x: (x[1], x[0]))
    
    converted_list = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), sorted_raw))
    
    output_path = "minutes.csv"
    
    with open(output_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"]) 
        writer.writerows(converted_list)     
        
    return converted_list


# Tasks 2, 3, 9
employees = read_employees()

employee_id_column = column_index("employee_id")

final_dict = all_employees_dict()

# Task 12 
minutes1, minutes2 = read_minutes()

# Task 13
minutes_set = create_minutes_set()

# Task 14
minutes_list = create_minutes_list()

# Task 15
final_sorted_minutes = write_sorted_list()