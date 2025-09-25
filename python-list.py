fruits = ["apple","orange","banana"]
print(fruits[0])

#used to add items in the list at last place
fruits.append ("watermelon")
fruits.append ("kiwi")

#used to add the item at particular place in index
fruits.insert(1,"graphe")

#used to remove the particular item (have to mention item name)
fruits.remove("orange")

# used to remove only the last item fron the list
fruits.pop()

#NESTED LIST......
mixed_fruits = [["apple","orange"],["almonds","nuts"],["water","juice"],"hello"]

#now i am replacing the orange from banana so the following sytanx is used to do so
mixed_fruits[0][1] = "banana"

print (mixed_fruits[0])
print (mixed_fruits[0][1])
print (mixed_fruits[3])
print(len(mixed_fruits))

