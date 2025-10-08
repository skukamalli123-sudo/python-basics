a = 10
name = "abcd"
isvalid = True
price = 10.5

if a == int("10"):# conversion type where 10.5 is coverted to int from float
    print("yes")
else:
    print("no")

if a == int(10):# it is same 
    print("yes")
else:
    print("no")

# tuples
config = ("user","root","pasword")
print(config[1])

# unpacking

a,b,c = config
print(a,b,c)

#dictionary
company = {
    "name":"shivakumar",
    "revenue":1000000,
    "address":{
        "name":"om nilyam",
        "pincoad":585104,
        "houseno":"#85"
    },
    "isproductbased":True,
    "directors":["shiv","kumar"],
    "description":""
}
print(company["name"])
print(company.get("ceo","damn"))

#adding information to keys present in dictionary

if company['isproductbased']:
    company.update({"description":"this is product based"})
else:
    company.update({"description":"this is not product based"})

    print(company["description"])

#forloop

nums = [1,2,3,4,5,6,7,8,9,10]
totalnums = 0
for num in nums:
    print(num)
#for getting total of all the item in list we use the following syntax
totalnums += num
print(totalnums)


#to seperate the odd and the even values we creat
even_values=[]
odd_values=[]

#for finding the even and odd no. we modules i.e %
for n in nums:
    if n%2==0:# dividing the list no. with 2 to check the odd or even 
       print(n,"even")
       even_values.append(n) #for seperatin the odd values we append it 
    
    else:
        print(n,"odd")
        odd_values.append(n) #for seperatin the odd values we append it 

print(even_values,odd_values)
