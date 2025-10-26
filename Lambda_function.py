lambda params: expression
# def add(a,b):
#     print(a+b)
# add(10,20)

# variable = lambda a,b: a+b
# print(variable(10,20))

# mul= lambda c,d: c*d
# print(mul(20,30))

# letters=[]
# letters = lambda letters: letters.append()
# print(letters("abcde"))

# letters = lambda letters: letters.upper()
# print(letters("abcde"))

# names = ['a','b','c']
# marks  = [10,20,30]
# zip(names,marks)
# type_cast = list(zip(names,marks))
# print(type_cast)

evenlist = []
for i in [1,2,3,4,5,6,7,8,9,10]:
    if i%2==0:
        print("even",i)
        evenlist.append(i)
    print(evenlist)


#LIST COMPREHENSION
l1 = [1,2,3,4,5,6,7,8,9,10]
filteredlist = [i for i in l1 if i%2==0]
[print(filteredlist)]