#for loop on list
for i in [1,2,3,4,5]:
    print(i)

#for loop on tuple
for i in (1,2,3,4,5):
    print(i)

#for loop for string
for i in "hello":
    print(i)

#for loop on dictionary
family = {
    'name':'a',
    'fname':'fa',
    'mname':'ma'
}

for fam in family:
    print(fam,family[fam])


Familylist = [
        {
        'name':'a',
        'fname':'fa',
        'mname':'ma'
        },
        {
        'name':'a1',
        'fname':'fa1',
        'mname':'ma1'
        },
        {
        'name':'a2',
        'fname':'fa2',
        'mname':'ma2'
        }
    ]

for flist in Familylist:
    print(flist['name'])
    if flist['name']=='a1': # by using this syntax we can skip the upadate opration 
        continue            # using continue key in the syntax 
    flist.update({'country':'india'})
    print(flist)

print("list",Familylist)

# countinue and Break

vowels = ['a','e','i','o','e']

countryname = "india"

for char in countryname:
    if char in vowels:  #To skip the vowels present in countryname we use coutinue.
            continue
    print(char)

for char in countryname:
    if char =='a':  #to stop the loop if it find the char== a we use break.
        break
    print(char)

print("i am outside")