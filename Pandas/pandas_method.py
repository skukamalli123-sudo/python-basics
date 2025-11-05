import pandas as pd

users = {
        "id" : [1,None,2,3,4,5,5,None],
        "name" : ["a",None,"b","c","d","e","e",None]
}

df = pd.DataFrame(users)
print(df)
df["age"]=[20,19,18,17,16,15,14,13]


# nullvalues = df.isna()
# print(nullvalues)

df = df.dropna()
df["lname"]=df["name"].apply(lambda name: len(name))
df["updatedage"] = df["age"].apply(lambda age : age+1)
df["name"] = df ["name"].apply(lambda name : name.upper())
df["age1"] = df ["age"].apply(lambda age:"even,TRUE" if age %2 == 0 else "odd,FALSE")
df["age_range"] =  [i for i in range(30,36)]


 
df = df.drop_duplicates()

df ["id"] = df ["id"].astype("int")
print(df)

import pandas as pd

data = {
    'Department': ['HR', 'IT', 'HR', 'Finance', 'IT', 'Finance', 'HR'],
    'Employee': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'Salary': [30000, 40000, 35000, 50000, 45000, 55000, 55000]
}

df = pd.DataFrame(data)
# df = df.groupby('Department').count()
df = df.groupby('Department')['Salary'].sum()
# df = df.groupby('Department')['Salary'].min()
print(df)


