fruits = ["apple","mango","banana"]

# if we use "for" in syntax it means it is a forloop
for fruit in fruits:
    print(fruit) # this syntax is used to print the loop of fruits as fruit if there is 3 item in list 
#then the loop run for 3 times to check it print it

    print(fruit,"is a fruit") # this syntax is used to add something to result here i added "is a fruit" 

    print(fruit, "length is",len(fruit))
    # the above syntax is used to print the length of particular item in list,

    if len(fruit) >= 6:
        print(fruit)
    # the above syntax is used to print the name of fruits having length >= to 6:

#date  09/10/2025
fruits = ["apple","mango","banana"]

for index,item in enumerate(fruits):
    print(index,item)
    print(index,item,len(item))

#for stopping the loop we use "break" function

numbers = [1,2,3,4,5]
for z in numbers:
    if z==2:
        print("yes found")
        break

print(z)

#Finding items in list
searchitem = 2
isfound = False
for num in numbers:
    if searchitem == num:
        isfound = True
        print("found")
        break

#for stopping the loop we use "break" function

names = ['a','b','c','d']
for character in names:
    print(character)
    if character =='c':
        break

print("Flitering words....")

dirtyword = ['fx','as','sx']
username = ['fx','as','sx','hi','hello','bye']

for u in username:
    if u not in dirtyword:
       print(u)

#print tables of any numbers
tablenumber = 20
tablenumupto = 20
for n in range(1,tablenumupto+1):
        print(n*tablenumber)