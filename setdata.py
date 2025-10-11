# sets are unorder, immutable, used to print the unique vales to remove duplicate in list or tuples

names = {"a","b","c","d",}
names.add("e")# adds item to sets
# names.remove("z")# removes values if exists otherwise through error
names.discard("a")# Remove the values if exists otherwise doesnt through error
print(names)


# for removing duplicate values we convert it to list,tuple
#because sets are inmutable 
fruits = ["apple","banana","apple","banana"]
unique_fruits = set(fruits)#converting fron list to set
unique_list_of_fruits = list(unique_fruits) # converting the got set result back to list
print(unique_fruits,unique_list_of_fruits)

#insted of writing this 11,12,13 line code we can simplfy it to following
unique_fruits = list(set(fruits))
print(unique_fruits)