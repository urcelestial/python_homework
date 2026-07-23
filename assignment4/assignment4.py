# TASK 1

import pandas as pd
import json

# Original Data

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25,30,35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

task1_data_frame = pd.DataFrame(data)
print(task1_data_frame)

# Making a New Column

task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [ 70000, 80000, 90000]

print(task1_with_salary)

# Modify an Existing Column

task1_older = task1_with_salary.copy()
task1_older['Age'] = task1_older['Age'] + 1
print(task1_older)

# Save the DataFrame to a CSV file
task1_older.to_csv('employees.csv', index=False)

saved_df = pd.read_csv('employees.csv')
print(saved_df)




# TASK 2

# Read data from the CSV file created in Task 1
task2_employees = pd.read_csv('employees.csv')
print(task2_employees)

# Read data from a JSON file
with open("additional_employees.json", "w") as file:
    json.dump([
        {'Name': 'Eve', 'Age': 28, 'City': 'Miami', 'Salary': 60000},
        {'Name': 'Frank', 'Age': 40, 'City': 'Seattle', 'Salary': 95000}
    ], file)

json_employees = pd.read_json("additional_employees.json")
print(json_employees)

# Combine the two DataFrames
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print(more_employees)



# TASK 3
first_three = more_employees.head(3)
print(first_three)

last_two = more_employees.tail(2)
print(last_two)

employee_shape = more_employees.shape
print(f"The shape of the DataFrame is: {employee_shape}")

print(more_employees.info())




# TASK 4

dirty_data = pd.read_csv('dirty_data.csv')
print(dirty_data)

clean_data = dirty_data.copy()

# Removing Duplicate Rows from the DataFrame
clean_data = clean_data.drop_duplicates()
print('Before Comversion')
print(clean_data)

# Convert Age to numeric and handle missing values
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors="coerce")
print('After Conversion')
print(clean_data)

# Convert Salary to numeric and replace known placeholders 
clean_data['Salary'] = clean_data['Salary'].replace('unknown', pd.NA)
clean_data['Salary'] = clean_data['Salary'].replace('n/a', pd.NA)

clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors="coerce")

print(clean_data)

# Fill missing numeric values (use fillna)
mean_age = clean_data['Age'].mean()
clean_data['Age'] = clean_data['Age'].fillna(mean_age)

median_salary = clean_data['Salary'].median()
clean_data['Salary'] = clean_data['Salary'].fillna(median_salary)

print(clean_data)

# Convert Hire Date to datetime
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], format='mixed', errors='coerce')
print(clean_data)

# Strip whitespace
clean_data = clean_data.map(lambda x: x.strip() if isinstance(x, str) else x)

# Convert Name and Department to uppercase
clean_data['Name'] = clean_data["Name"].str.upper()
clean_data['Department'] = clean_data["Department"].str.upper()

print('FINALIZED CLEAN DATA')
print(clean_data)
