# def print_nums(n):
#     for item in range(1,n+1):
#         print(item)
# print_nums(10)

# start =1
# def print_nums1(num):
#     global start
#     print(start)
#     start +=1
#     if start<=num:
#         print_nums1(num)
# print_nums1(5)


# def hello(name):
#     print("hello",name)
# hello1 = hello
# hello1("shiva")

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
def mod(a,b):
    print("mod of two no.")
    print(a%b)
def power(a,b):
    print("power of two no.")
    print(a-b)
def square(a,b=None):
    print("square of two no.")
    print(a*a)

operation_type = {
    "add":add,
    "sub":sub,
    "mul":mul,
    "div":div,
    "mod":mod,
    "power":power,
    "square":square 
}

def calculate(a=10,b=20,opty="add"):
    call_back= operation_type[opty]
    call_back(a,b)

calculate(2,3,"square")