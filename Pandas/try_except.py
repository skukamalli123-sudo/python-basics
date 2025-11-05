import pandas as pd

try:
    df = pd.read_csv('Hospital_Data.csv') 
    df['average'] = df['Patients Count'].mean()
    print(df)
except Exception as e:
    print("issue")
    print(e)
finally:
    print('successfully running......')






