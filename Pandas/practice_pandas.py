import pandas as pd

data = {
    'Name': ['John', 'Priya', 'Alex', 'Sara', 'Ravi', 'Meena', 'Arun', 'Bina'],
    'Department': ['HR', 'Finance', 'IT', 'Finance', 'IT', 'HR', 'Finance', 'IT'],
    'Salary': [50000, 65000, 70000, 62000, 72000, 52000, 60000, 71000],
    'Experience': [3, 5, 4, 6, 7, 2, 3, 5],
    'Gender': ['M', 'F', 'M', 'F', 'M', 'F', 'M', 'F']
}

df = pd.DataFrame(data)
print(df)

# dispay the first row of data set
df_head = df.head(5)
print(df_head)

# total number of rows and column
df_shape = df.shape
print("TOTAL NUMBER OF ROWS AND COLUMNS")
print(df_shape)

# display the name and salary column
column = df[["Name","Salary"]]
print("||||selected only name and salary column")
print(column)

#Sort the the employees by Salary in descending order
df.sort_values (by=['Experience'],ascending = True, inplace= True)
print("SORTED_VALUE IN ASCENDING")
print(df)

# Find the average salary of all the employee
average_salary = df['Salary'].mean()

print("AVERAGE_SALARY",average_salary)

#Show employees whoes department is IT
IT_employee = df[(df['Department'] == 'IT') & (df['Experience'] >=5)]

print("DEPT_EXPERIENCE >= 5")

print(IT_employee)

IT_DEPT_SAL= df[(df['Department'] == 'IT') | (df['Salary'] > 70000)]

print("DEPT_SALARY > 70000")

print(IT_DEPT_SAL)

#List employees whose Salary is greater than 65000
employees = df[df['Salary']>65000]
print ("SALARY IS GREATER THAT 65000")
print(employees)

#Display names of employees with Experience greater than or equal to 5
experience = df[df['Experience']>=5]

print("EXPERIENCE GREATER THAN 5 YEARS")
print(experience)

#GroupBy & Aggregation

#Find the average Salary in each department
AVG_SALARY = df.groupby('Department')['Salary'].mean()
print("AVERAGE_SALARY")
print(AVG_SALARY)

##Find the total Salary in each department
TOTAL_SALARY = df.groupby('Department')['Salary'].sum()
print(TOTAL_SALARY)
 
# USE OF nlargest to find the 2nd largest salary
second_highest_slary = df['Salary'].nlargest(2)

print("GROUPBY AND 2ND LARGEST SALARY")
print(second_highest_slary.min())

# TO COUNT THE NUMBER OF ELEMNTS IN THE DATEFRAME
count_values = df['Department'].value_counts()
print("REPETATIVE WORD IN THE COLUMN DEPARTMENT")
print(count_values)

query = df.query("(Department == 'HR' & Salary >50000) or (Department == 'IT' & Salary >50000)")
print(query)