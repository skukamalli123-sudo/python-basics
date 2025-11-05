import pandas as pd

data1 = pd.DataFrame({
    "name":['sunil','shivu','mahadev'],
    "age":[29,28,29]

})

def result(age):
    if age %2==0:
        return "even"
    else:
        return "odd"
data1['even_odd'] =data1['age'].apply(result)
print(data1)