fruits = ["apple","orange","banana"]
print(fruits[0])

#used to add items in the list at last place
fruits.append ("watermelon")
fruits.append ("kiwi")
print(fruits)

#used to add the item at particular place in index
fruits.insert(1,"graphe")
print(fruits)

#used to remove the particular item (have to mention item name)
fruits.remove("orange")
print(fruits)


# used to remove only the last item fron the list
fruits.pop()
print(fruits)

# used to remove particular item present at particular index value i.e 0 = apple thats why after
#printing it will remove the item present at index value 0
fruits.pop(0)
print(fruits)

#NESTED LIST......

mixed_fruits = [["apple","orange"],["almonds","nuts"],["water","juice"],"hello"]

#now i am replacing the orange from banana so the following sytanx is used to do so
mixed_fruits[0][1] = "banana"

print (mixed_fruits[0])
print (mixed_fruits[0][1])
print (mixed_fruits[3])
print(len(mixed_fruits))

