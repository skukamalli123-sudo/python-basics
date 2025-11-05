def greet(name, is_morning):
    if is_morning:
        print ("Good morning",name)
    else:
        print ("Good evening",name)

print(greet("shiva",False))

def add(a,b,showresult):
    if showresult == "add" :
        print(a+b)
    else:
        print("no add")    

add(10,10, "add")