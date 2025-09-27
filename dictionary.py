# person = {
#     "name":"shivu",
#     "age":20,
#     "company":"abc",
#     "hobbies":["reading,writting"],
#     "salary":10000,
#     "ismarried":True
# }
# the above block is dictionary where person = person dictionary variable where as name,age,comany,hobby ect
#are the keys of dictionary shivu 20 abc ect are the values.and it is written in flower bracket 


#LIST OF DICTIONARY.....

#the below code has the list of block it may be n no. of valuesand n no. blocks in it starts with the array bracet 
#follwed by flower bracket like [{block1},{block2},{block3}]
persons = [{
    "name":"shivu",
    "age":20,
    "company":"abc",
    "hobbies":["reading,writting"],
    "salary":10000,
    "ismarried":True
},

    {
    "name":"mahi",
    "age":26,
    "company":"abc",
    "hobbies":["writting"],
    "salary":10000,
    "ismarried":True
}
]
shivinfo,mahiinfo = persons
print(persons)
print(shivinfo)
print(shivinfo['name'])
print(mahiinfo['salary'])