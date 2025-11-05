import pandas as pd

hr_data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Department": ["HR", None, "Finance", "Marketing", None],
    "Salary": [50000, None, 55000, 65000, None],
    "Experience_Years": [2, 3, 5, 4, 6],
    "Date_of_Joining": ["2021-05-10", None, "2020-03-22", "2022-08-15", None],
    "Age": [25, None, 30, 28, None]
}

def loggingdata(df,msg,showdf = True):
    print(msg)
    if showdf:
        print(df)
        return df
    

def Cleand_data(hr_data):
    df = (
        pd.DataFrame(hr_data)
        .pipe (loggingdata,"creating dataframe",True)
        .query("(Age.notna()) and (Department.notna())")
        .assign(Name = lambda df:df['Name'].str.upper())
        .pipe (loggingdata,"converting the name into upper string",True)
        .assign(average = lambda df:df['Salary'].mean().astype("int"))
        .assign(Total_salary = lambda df:df.groupby('Department')['Salary'].transform("sum"))
        .pipe (loggingdata,"done trosfor using sum",True)
        .sort_values(by=['Salary'])

        )
    
    return df

print("AFTER CHAIN METHOD")
print(Cleand_data(hr_data))