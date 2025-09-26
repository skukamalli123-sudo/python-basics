#REVERSE INDEX.....
#here the indexing is done in reverse order where f=-1,e=-2 total e,f = -1 from forward if consider
name = ['a','b','c',['e','f']]
print(name[-1][-2])
print(name[-2])

#SLICING......
fruits = ('apple','banana','mango')
print(fruits[0:2])
print(fruits[:3])
print(fruits[0:])
print(fruits[0:10])

# IS operatore in list 

list1 = [1,2,3]
list2 = [1,2,3]
list3 = list1

print(list1 == list2) #compares the values by using ==
print(list1 is list2) #compares the address(the reference id  is same for list1 and list 2)
print(list1 is list3)

#COUNT NUMBERS OF ITEM IN LIST

countnumb = (1,2,3,4,5,6,6,6,6,7,7,8)
#the following syntax is used print juz the item present in list
print(countnumb)
# to find the how many times the particular number is present in the list we use the following syntax
print(countnumb.count(6))


#IN OPERATORE IN LIST....
#1 EXAMPLE
countnumb = (1,2,3,4,5,6,6,6,6,7,7,8)
if 6 in countnumb:
    print("yes")
else:
    print("no")

#2 EXAMPLE
allowescountries = ['ind','sri','pak','ban']
newcountry = 'uk'
if newcountry in allowescountries:
    print("allowed")
else:
    print("not allowed")
