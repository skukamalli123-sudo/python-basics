import pandas as pd 

series = pd.Series([1,2,3,4])
print(series)

user= {
    "name":["x","y","z","a","b","c"],
    "email":["x@","y@","Z@","A@","B@","C@"]

}

dictionary = pd.DataFrame(user)
print(dictionary)
print(dictionary.head())
print(dictionary.tail())