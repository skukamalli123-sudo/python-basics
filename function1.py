def add(a,b):
    print("addition of two no.")
    print(a+b)
def sub(a,b):
    print("sub of two no.")
    print(a-b)
def mul(a,b):
    print("multiplcation of two no.")
    print(a*b)
def div(a,b):
    print("division of two no.")
    print(a/b)

#  WITH DEFALUT PARAMETER

def calculateversion1(a =10,b=20,optype ="mul"): #optype is a operator type.
    if optype == "add":
        add(a,b)
    elif optype == "sub":
        sub(a,b)
    elif optype == "mul":
        mul(a,b)
    elif optype == "div":
        div(a,b)
    else:
        print("invalid opty")
# calculateversion1(10,20,"add")
# calculateversion1(10,20,"mul")
# calculateversion1(10,20,"xyz")
calculateversion1()

# WITHOUT PREDEFINED PARAMETERS

def calculateversion2(a,b,optype): #optype is a operator type.
    if optype == "add":
        print(a+b)
    elif optype == "sub":
        print(a-b)
    elif optype == "mul":
        print(a*b)
    elif optype == "div":
        print(a/b)
    else:
        print("invalid opty")
# calculateversion2(20,20,"add")
# calculateversion2(20,20,"mul")
# calculateversion2(20,20,"xyz")

# #GLOBAL OPERATORE IN FUNCTION  

total = 10 # this total is present in global location
def abcd():
    global total #by use GLOBAL operator we are making that global "total" to local,means in function 
                 #then we can use the global variable in local variable
    total = total+30
    print(total)

abcd()