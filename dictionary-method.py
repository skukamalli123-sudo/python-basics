emp = {
    "name":"shivu",
    "email":"smk@gmail.com"
}
#ACCESSING THE VALUES FROM DICTIONARY
name1 = emp.get('name')
email1 = emp.get('email')

print(name1,email1)

#UPADATEING THE VALUES FROM DICTIONARY

emp.update({"mobile":"9663209599"})
emp.update({"ismarried":False})

print(emp)

#REMOVING ISMARRIED FROM DICTIONARY AND RETRUNS IT VALUES

value = emp.pop("ismarried")
print(emp)
print(value)